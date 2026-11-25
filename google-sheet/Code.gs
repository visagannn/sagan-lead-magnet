/**
 * Checklist Ganti Gaji → Google Sheet
 *
 * Receives one row per visitor from check.saganproductions.com and keeps it up to date
 * (Siap → Hantar WA). The Instagram checklist goes to the "Leads" tab; the LinkedIn
 * SME audit (check.saganproductions.com/sme) goes to its own "SME Leads" tab. Paste this whole file into the sheet's Extensions → Apps Script,
 * then Deploy → New deployment → Web app (Execute as: Me, Who has access: Anyone).
 * Setup steps are in the README, section "Google Sheet".
 *
 * It also keeps an anonymous "Visits" tab (time, page, step, ?dari= tag; no name or number)
 * so the dashboard can show how many people opened the page and started answering, and it
 * emails the sheet owner (the Google account that deploys this script) once for each new lead.
 *
 * Nothing secret here: the page's link to this script is public anyway, so the script
 * only ever adds or updates rows, checks every value, and never reads anything back.
 */

const TAB = "Leads";
const HEAD = ["ID", "Mula", "Kemas kini", "Nama", "No. telefon", "WhatsApp", "Umur", "Jantina", "Dari",
  "Status", "Kerja", "Loan rumah", "Settle", "Jurang", "Tak pasti", "Senarai jurang"];
// Contacted / Replied / Closed are set by Sagan from the leads dashboard; a visitor coming back never moves a lead back down
const RANK = {"Mula": 1, "Siap": 2, "Hantar WA": 3, "Contacted": 4, "Replied": 5, "Closed": 6};
const SME_TAB = "SME Leads";
const SME_HEAD = ["ID", "Mula", "Kemas kini", "Name", "Mobile", "WhatsApp", "Company", "Role", "From",
  "Status", "Business type", "Employees", "In place", "Gaps", "Not sure", "Gap list"];
const VISIT_TAB = "Visits";
const VISIT_HEAD = ["Masa", "Page", "Step", "Dari"];
const STEPS = {"buka": 1, "jawab": 1};   // buka = opened the page, jawab = answered the first question

function doPost(e) {
  const out = ContentService.createTextOutput("ok");
  let d;
  try { d = JSON.parse(e.postData.contents); } catch (err) { return out; }

  // Anonymous visit counts: one row per phone per step, nothing personal
  if (d.visit) {
    if (STEPS[d.visit]) sheet_(VISIT_TAB, VISIT_HEAD).appendRow([new Date(), d.form === "sme" ? "sme" : "gaji", d.visit, clean_(d.dari, 40)]);
    return out;
  }

  // Basic checks, so random posts can't fill the sheet with junk
  const id = String(d.id || "");
  const tel = String(d.tel || "");
  if (!/^[a-z0-9]{6,20}$/.test(id) || !/^601\d{8,9}$/.test(tel) || !RANK[d.status]) return out;

  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  let isNew = false;
  try {
    const sme = d.form === "sme";
    const sh = sheet_(sme ? SME_TAB : TAB, sme ? SME_HEAD : HEAD);
    const now = new Date();
    const found = sh.getRange("A:A").createTextFinder(id).matchEntireCell(true).findNext();
    const rowNo = found ? found.getRow() : sh.getLastRow() + 1;
    isNew = !found;
    const old = found ? sh.getRange(rowNo, 1, 1, HEAD.length).getValues()[0] : null;
    // Status only moves forward: someone who already sent to WhatsApp stays "Hantar WA"
    const status = old && (RANK[old[9]] || 0) > RANK[d.status] ? old[9] : d.status;
    sh.getRange(rowNo, 1, 1, HEAD.length).setValues([[
      id,
      old ? old[1] : now,
      now,
      clean_(d.nama, 40),
      "+" + tel,
      "https://wa.me/" + tel,
      sme ? clean_(d.syarikat, 60) : clean_(d.umur, 2),
      sme ? clean_(d.peranan, 20) : clean_(d.jantina, 10),
      clean_(d.dari, 40),
      status,
      sme ? clean_(d.jenis, 20) : clean_(d.kerja, 30),
      sme ? clean_(d.staf, 10) : clean_(d.loan, 10),
      clean_(d.settle, 7),
      Number(d.jurang) || 0,
      clean_(d.tak_pasti, 500),
      clean_(d.senarai, 1000),
    ]]);
  } finally {
    lock.releaseLock();
  }
  if (isNew) alert_(d, tel);
  return out;
}

// One email to the sheet owner per new lead. Goes only to the account that deployed this script.
function alert_(d, tel) {
  try {
    const sme = d.form === "sme";
    const name = clean_(d.nama, 40) || "Someone";
    const lines = [
      name + (sme ? " just did the SME Benefits Gap Audit." : " baru buat Checklist Ganti Gaji."),
      "",
      "WhatsApp: https://wa.me/" + tel,
      sme ? "Company: " + clean_(d.syarikat, 60) + " (" + clean_(d.peranan, 20) + ")" : "Umur: " + clean_(d.umur, 2) + ", " + clean_(d.jantina, 10),
      sme ? "Business: " + clean_(d.jenis, 20) + ", " + clean_(d.staf, 10) + " staff" : "Kerja: " + clean_(d.kerja, 30) + ", loan rumah: " + clean_(d.loan, 10),
      "Jurang: " + (Number(d.jurang) || 0) + " (" + clean_(d.settle, 7) + " settle)",
      "Dari: " + (clean_(d.dari, 40) || "-"),
      "",
      "Sheet: " + SpreadsheetApp.getActiveSpreadsheet().getUrl(),
    ];
    MailApp.sendEmail({
      to: Session.getEffectiveUser().getEmail(),
      subject: (sme ? "New SME lead: " : "Lead baru: ") + name + " (" + (Number(d.jurang) || 0) + " jurang)",
      body: lines.join("\n"),
    });
  } catch (err) { /* the row is saved even if the email fails (e.g. daily limit) */ }
}

// A tab, made with a header row the first time
function sheet_(name, head) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    sh.appendRow(head);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, head.length).setFontWeight("bold");
    if (head[0] === "ID") {               // leads tabs: hidden ID column, dates in B and C, phone as text
      sh.getRange("B:C").setNumberFormat("d mmm yyyy, h:mm am/pm");
      sh.getRange("E:E").setNumberFormat("@");
      sh.hideColumns(1);
    } else {
      sh.getRange("A:A").setNumberFormat("d mmm yyyy, h:mm am/pm");
    }
  }
  return sh;
}

// Plain text only: trims, shortens, and stops a value being read as a formula
function clean_(v, max) {
  let s = String(v == null ? "" : v).replace(/[\r\n\t]+/g, " ").trim().slice(0, max);
  if (/^[=+\-@]/.test(s)) s = "'" + s;
  return s;
}

// Run this once from the editor (▶ Run) to check it works: it adds a test row you can delete after
function testRow() {
  doPost({postData: {contents: JSON.stringify({id: "test" + Date.now().toString(36), nama: "Ujian", tel: "60123456789",
    umur: "30", jantina: "Lelaki", dari: "ujian", status: "Mula", kerja: "dengan majikan", loan: "ada",
    settle: "4/16", jurang: 12, tak_pasti: "Medical card sendiri", senarai: "Penama KWSP"})}});
}

// Test for the Visits tab: adds one "buka" row
function testVisit() {
  doPost({postData: {contents: JSON.stringify({visit: "buka", form: "gaji", dari: "ujian"})}});
}

// Same test for the SME audit tab
function testRowSme() {
  doPost({postData: {contents: JSON.stringify({form: "sme", id: "test" + Date.now().toString(36), nama: "Test", tel: "60123456789",
    syarikat: "Test Sdn Bhd", peranan: "Owner / Director", dari: "test", status: "Siap", jenis: "Sdn Bhd", staf: "6–20",
    settle: "5/14", jurang: 9, tak_pasti: "Key-person cover", senarai: "Group medical plan"})}});
}
