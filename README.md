# Checklist Ganti Gaji (free lead magnet)

Live at **https://check.saganproductions.com** (GitHub Pages, repo `visagannn/sagan-lead-magnet`, DNS at GoDaddy: `CNAME check → visagannn.github.io`).

One phone page, one question: **"Kalau esok korang tak boleh kerja, apa yang ganti gaji korang?"**

16 things to tick in 5 sections (13 to 16 after the two opening questions). What they can't tick is the gap, and the only next step is WhatsApp. Free to run: no backend, no database, no paid tools.

The Cek Perlindungan calculator that used to be at this address is off the site. Its improved version is kept on the local git branch `kalkulator-v2` (not pushed).

## Two pages, two markets

| Page | Address | For | Language |
| --- | --- | --- | --- |
| **Checklist Ganti Gaji** (`index.html`) | `check.saganproductions.com` | Individuals, from Instagram | Malay ("korang") |
| **SME Benefits Gap Audit** (`sme/index.html`) | `check.saganproductions.com/sme/` | SME owners and HR, from LinkedIn | English |

Both use the same white design and the same code, but they are separate files: a design or behaviour change has to be made in both. Most of this README describes the Instagram page; the SME page has its own section near the end.

## Sections

1. **Kalau MC lama** (3): paid sick leave, 3 months of savings, KWSP Akaun Fleksibel.
2. **Kalau kemalangan atau hilang upaya** (3): what PERKESO pays for accidents, what PERKESO and KWSP pay for permanent invalidity, TPD in their takaful plan.
3. **Kalau sakit kritikal** (3): own medical card, critical illness cover that pays cash, contribution-waiver rider.
4. **Kalau korang tiada** (5): own life cover, KWSP nominee, hibah nominee, MRTT/MLTT, partner knows where the documents are.
5. **Supaya pelan tak lupus** (2): contributions can rise with age, full health declaration.

**Opening** (25 Nov 2026 copy): label "AUDIT GANTI GAJI · 16 PERKARA", "Kalau esok korang tak boleh kerja," / **"Berapa lama duit korang bertahan?"** (coral marker underline that wraps on phones), the line "Ramai ingat kad medical company + PERKESO dah cukup…" and "100% Percuma · Tak perlu call · Setiap fakta ada sumber rasmi". No form here: visitors go straight into the questions.

**Two quick questions** ("LANGKAH 1 · 10 SAAT", optional, with a marker drawing that changes with the answer: a question mark, an office worker holding a GAJI envelope, a stall owner at their KEDAI, a delivery rider; plus a house marked LOAN when they have a house loan): "Korang kerja macam mana?" (kerja dengan majikan / kerja sendiri / gig) and "Ada loan rumah?". Self-employed and gig workers don't see the Employment Act sick-leave item, and two items change wording for them ("Ada medical card sendiri", "Ada perlindungan hayat sendiri", without the company/employer parts; set in `alt` on each item). No house loan hides MRTT. The answers go into the WhatsApp message.

**Form before the result** ("LANGKAH TERAKHIR · Nak tengok keputusan? Isi ni dulu."): Nama, No. telefon (WhatsApp), Umur and Jantina, plus a tick box "Saya setuju Sagan WhatsApp saya untuk semakan jurang ni (tiada spam)." All are required; the result and the offer stay hidden until they press **Tengok keputusan**. The number must be a Malaysian mobile (01x…, with or without +60) and age 16 to 80. A hidden field catches bots. Returning visitors on the same phone skip it. The bottom bar and "Tengok keputusan ↓" take them to this form while it's locked. If `SHEET` is set, pressing it adds them to your Google Sheet as **Siap**.

Each item has a title and a one-line summary in plain words, then **"Lihat fakta & sumber ›"**: opens a short fact (one or two lines) on a taped paper index card over the blurred page, with the official sources named as plain text (not links) and a **"Tak pasti"** button. "Tak pasti" puts a red "?" in the box; ticking the box replaces it.

Design is colour-blocked like the reels and like high-converting lead-magnet pages: full-width bands in deep wine, charcoal and off-white, with AIA crimson only for emphasis (no pink: hand-drawn strokes in AIA red #E3173D, small labels in warm off-white) (the style bible's palette: charcoal, muted olive, off-white, subtle red; yellow was dropped because red + yellow read as fast food), with white cards on top for depth. The opening is a near-black band (white headline, red hand-drawn underline) with the two questions as a white card. Each section is a white card with a coloured header strip (crimson, charcoal, olive, wine, graphite) and its marker drawing as a tilted white sticker. The result is a charcoal band with the number circled in red. Gap cards carry their section colour on top. The WhatsApp box is a wine band with a white form card and a white button with crimson text. The small print sits in a dark footer band. Inter, crimson #D30A32, ink #18181B; a faint dot grid on the cream page.

**Doodle style:** a faint chalk-doodle wallpaper (stars, swirls, arrows, hearts, umbrellas, houses, RM, clouds), headings in the clean bold font for easy reading, a second crooked chalk outline around each card, and handwritten notes with arrows that draw themselves ("jawab 2 ni dulu!", "ni jurang korang", "percuma je!").

**Look (v3, 25 Nov 2026): white, bold and simple, in the style of Alex Hormozi's lead-magnet pages (the style only; the words, drawing and colours are ours).** White page, heavy black Poppins headlines, **AIA red `#D31145`** (taken from aia.com.my's own stylesheet; `#A80D37` is the darker shade for pressed buttons), clean bordered cards. The hero is centred: a pill label with a green dot ("AUDIT GANTI GAJI PERCUMA · 16 PERKARA"), the headline, a wide marker drawing (salary going into a bucket marked GAJI that leaks, with one leak circled in red and labelled JURANG), a trust line, and a 3-step strip (Tick 16 perkara → Nampak jurang korang → Semakan percuma dengan Sagan). There is no "X people have used this" line because we have no real number yet; add one only when it's true. The offer at the end is one dark card with a white WhatsApp button. On a computer the hero and the top bar go wide; on a phone the steps stack. The dark chalkboard look (v2) is in git history before commit "White Hormozi-style look".

**The stickman in the top bar.** A tiny stickman walks along the progress line. "Soalan 7 / 16" counts the furthest item they have actually answered (ticked or "Tak pasti"); scrolling alone doesn't move it. He hops when they tick, tilts with a "?" when they press Tak pasti, and cheers at the flag when the last item is answered. The 01–05 buttons jump to each section. Every drawing draws itself stroke by stroke the first time it comes on screen. With reduced motion on, drawings simply appear and he doesn't hop.

## Getting people through it

- **Section shortcuts** (01–05) in the top bar: tap to jump; a section turns red when fully settled; the one on screen is underlined.
- **Hint** before the first item: tick if you have it, "Tak pasti" if unsure, "Lihat fakta" to learn more.
- **Red pen tick** over a section's drawing when the whole section is settled.
- **"Hampir siap. Tengok keputusan ↓"** appears above the bottom bar in the last two sections, until the result is on screen.
- **"Korang dah settle 5/13 sebelum ni. Sambung ↓"** for returning visitors, which jumps to the first unanswered item.
- The page is always dark (chalkboard), on every phone.
- Accessibility: fine print darkened for contrast, section shortcuts have spoken labels, keyboard focus stays inside the fact pop-up.
- **Pop-ups: a stickman talking.** Every pop-up is a white comic speech bubble with a chalk stickman standing under its bottom-right corner. Facts are 1–2 lines; official sources show as plain text ("Sumber: …"), not links.
- **Reminder before leaving.** Once they have answered at least 2 items, pressing back (or, on a computer, moving the mouse to the top of the window) shows one reminder per visit: "Eh, dah nak pergi? Tinggal N perkara je lagi…" with **Sambung** (jumps to the next item) or **Keluar** (leaves; a second back also leaves). If every item is answered, it asks them to send the list to Sagan instead. It never shows after they press the WhatsApp button. Browsers don't allow a custom message when a tab is closed, so closing the tab or the app is not caught.
- **Nothing ticked yet:** the result says "Belum semak lagi", the bottom bar says "Mula dari atas ↑", the button says "WhatsApp Sagan", and the message doesn't list 16 gaps.
- **Result filter:** "Ni peta jurang gaji korang." has Semua / Belum ada / Tak pasti tabs with counts.
- **Link tag kept:** the first `?dari=` tag is saved on the phone, so a reload or later visit still reports where they first came from.
- **WhatsApp link:** `api.whatsapp.com/send?phone=…&text=…` (hands over more reliably from the Instagram browser). "Salin mesej" shows "Disalin ✓".

## The result

- Big number of gaps ("jurang"), including how many are "tak pasti", and the section with the most gaps.
- A marker drawing next to the number: dry under an umbrella with 3 gaps or fewer, a leaking umbrella with more (an illustration, not a score).
- Progress per section.
- Then **Jurang perlindungan korang** as one card per section that still has gaps, each with its own marker drawing, the number of gaps and the open items as chips ("tak pasti" chips are dashed red with a ?).
- The WhatsApp box says what they get, free: a review of the policies they already have (they send photos of their certificates) and a proposal to close each gap within their budget, with a same-day reply. These are Sagan's own promises (chosen 24 Nov 2026).
- **Maklumat korang** inside the WhatsApp box: Nama, Umur, No. telefon and Jantina, already filled in from the form before the result (they can change them; changes go both ways). Name and age go into the message ("Hi Sagan, saya Aina. …" then "Umur: 32 · Perempuan"). The offer reads "Nak tahu mana satu boleh settle percuma, dan mana satu kena tutup?" and the message ends "Boleh tolong semak jurang ni dan cadangkan apa yang patut saya tengok dulu?"
- The bottom bar's button ("Hantar ke Sagan") scrolls to this form instead of opening WhatsApp straight away, so more people fill it in.
- The WhatsApp box comes last. One WhatsApp button at a time: the floating bar is there while ticking and reading the gap cards, and slides away only once the big WhatsApp button at the end is on screen.
- WhatsApp fallback: 1.5 s after the tap a box shows the number and a "Salin mesej" button.
- Ticks, "tak pasti" and the two answers are saved in the visitor's own browser so they can come back. Nothing is sent unless they tap WhatsApp.

The WhatsApp message, kept short:

```
Hi Sagan, saya dah buat Checklist Ganti Gaji.
Kerja: sendiri · Loan rumah: tiada
Dah settle: 4 / 13

Tak pasti (2):
- TPD dalam pelan takaful
- Penerima hibah takaful

Belum ada (7):
- Kalau MC lama: Akaun Fleksibel KWSP
- Kalau sakit kritikal: Penyakit kritikal bayar tunai, Rider tak perlu bayar caruman
...

Boleh tolong semak polisi saya dan cadangkan cara tutup jurang ni?
Saya boleh hantar gambar sijil yang saya ada.
(dari: ig)
```

Start your reply with the "Tak pasti" items: they are questions the person already wants answered.

## Settings (top of the `<script>` in `index.html`)

| Constant | What it does |
| --- | --- |
| `WHATSAPP` | Number the button opens: `60176190139`. |
| `NAME` | Short name in the WhatsApp greeting and buttons. |
| `AGENT` | Your full registered agent name. Empty = the page shows `NAME`. Fill this in (see below). |
| `TITLE` | Your title, shown in the small print: Corporate Wealth & Takaful Consultant. |
| `CODE` | Your agent code, shown in the small print: 1353Z. |
| `SHEET` | The Google Sheet "Web app" link (see **Google Sheet** below). Empty = nothing is sent to a sheet; the page still works. |
| `REASON` | One **honest** reason to act now, e.g. a real weekly limit. Empty = not shown. Never invent one. |

## Links to use

Add `?dari=` and a short tag to every link. The tag shows at the end of the WhatsApp message, so you know which post brought each lead (there is no other tracking).

| Where | Link |
| --- | --- |
| Instagram bio | `https://check.saganproductions.com/?dari=bio` |
| Threads bio | `https://check.saganproductions.com/?dari=threads` |
| TikTok bio | `https://check.saganproductions.com/?dari=tiktok` |
| Instagram Story link sticker | `https://check.saganproductions.com/?dari=story` |
| Comment-to-DM reply | `https://check.saganproductions.com/?dari=dm` |
| A specific reel or carousel | `https://check.saganproductions.com/?dari=reel-perkeso` (name it after the post) |
| WhatsApp status / broadcast | `https://check.saganproductions.com/?dari=wa-status` |

Use lowercase letters, numbers and dashes only.

### Comment-to-DM and Story replies (free, in Meta Business Suite)

Both are on, under **Meta Business Suite → Inbox → Automations**, for Instagram and the Facebook Page:

| Automation | Trigger | Link it sends |
| --- | --- | --- |
| Comment to message – Checklist Ganti Gaji (SEMAK) | A comment containing SEMAK / semak / Semak / check / Check / gaji / Gaji / INCOME PROTECTION / Income protection / income protection (Meta's limit is 10) | `https://check.saganproductions.com/?dari=dm` |
| Custom keywords – DM SEMAK (Stories) | A DM or Story reply containing SEMAK / semak / Semak | `https://check.saganproductions.com/?dari=story` |

The comment version also replies publicly: "Dah hantar DM! Tak nampak? Tengok dalam Message Requests."
Instagram allows one private reply per comment, within 7 days. The DM keyword reply only fires when the chat
has been quiet for 15 minutes. Meta changes these menus often, so the names may differ slightly.

## To publish a change

Edit `index.html`, then in this folder:

```
git add -A && git commit -m "what changed" && git push
```

The live site updates in about a minute.

## Where the facts come from

All figures were read on **24 Nov 2026** from the official pages in `SOURCES` inside the file, and re-read by a second independent check. To change a figure, change it together with its source.

- AIA PUBLIC Takaful's site shows **no monthly "income replacement" plan**. Income protection in takaful comes from cash payouts (death, TPD, critical illness) and riders that keep contributions paid, so the page never promises a monthly income benefit.
- Do not use the "RM60–90 bilion harta beku" figure (private estimates only), or any AIA protection-gap statistic (the newest official ones are from 2015).

### Added 24 Nov 2026: richer hibah and medical card facts

Researched from official sources the same day (sources 15 and 17 to 24 in `SOURCES`):
- **Hibah:** nominate from age 16, a witness aged 18+ who is not a nominee, benefit not part of the estate or used for debts, nomination changed or revoked in writing but not by a will, a nominee who dies first loses their share to the estate, RM100,000 limit without a nominee (IFSA 2013 Sch 10). Not distributed by faraid (BNM Shariah Advisory Council). A will (wasiat) covers only 1/3 (Mufti Wilayah Persekutuan).
- **Medical card:** company cover isn't portable (AIA); example plan limits (RM1.5m/RM3m a year, no lifetime limit, RM200/RM300 room) from the A-Plus Health360-i brochure; BNM's required co-payment option (RM500 deductible and/or 5% co-takaful) and waiting-period caps (30 / 120 days); BNM's Dec 2024 measure to spread repricing over at least 3 years until end-2026; tabarru' rises with age (A-Plus Health360-i FAQ); 15-day free-look; tax relief RM4,000 for YA 2025.

Could not confirm, so left out: the A-Plus Health360-i grace period in days, a BNM deadline (in days) for paying death claims, and YA 2026 tax relief.

## Google Sheet (your leads list)

Every visitor who presses **Mula checklist** gets one row in a Google Sheet in your own Google account. The row updates as they go, so you can see who started but didn't finish:

| Column | What it shows |
| --- | --- |
| Mula / Kemas kini | When they started, and their latest change |
| Nama, No. telefon, Umur, Jantina | From the start form |
| WhatsApp | Tap to open a chat with them |
| Dari | The `?dari=` tag of the link they used (ig, dm, reel-…) |
| Status | **Siap** (filled the form to see the result) → **Hantar WA** (pressed the WhatsApp button). It never goes backwards. "Mula" was used when the form was at the start; since 25 Nov 2026 it stays at 0 on the Dashboard. |
| Kerja, Loan rumah | Their answers to the 2 questions |
| Settle, Jurang | e.g. 4/16 settled, 12 gaps |
| Tak pasti, Senarai jurang | The items they marked unsure, and the rest of their gaps |

Ticks are sent when they reach the result, press WhatsApp, or leave/switch apps. "Hantar WA" means they pressed the button; it can't tell whether they actually pressed send inside WhatsApp. To download it as Excel: **File → Download → Microsoft Excel**.

**The sheet already exists:** "Leads Checklist Ganti Gaji" in your Google Drive (made 25 Nov 2026; open it from Google Drive). It has two tabs:
- **Dashboard**: total leads, today, last 7 days, how many pressed WhatsApp, how many need follow-up; counts by status, by `?dari=` tag and by kind of work; the most common gaps with bars; and a follow-up list (everyone who hasn't pressed WhatsApp yet, newest first, with a tap-to-chat link). Everything updates by itself. Hidden columns K:L hold the item names the gap count uses; if an item's short name changes in `index.html`, change it there too.
- **Leads**: one row per visitor (columns above), with a filter on the header row. "Mula" rows are pink, "Hantar WA" rows green.

**Connected and live since 25 Nov 2026.** The script is in the sheet (Extensions → Apps Script), deployed as a web app ("Checklist leads", execute as the sheet owner, access: Anyone), and its link is in `SHEET` in `index.html`. Tested end to end from the live page. The Dashboard status block now reads "Isi borang, nampak keputusan" (Siap, plus any old Mula rows), "Tekan WhatsApp", and the share who pressed WhatsApp.

**If you ever set it up again (about 5 minutes, you do the sign-in):**
1. Open the sheet.
2. **Extensions → Apps Script.** Delete what's there, paste the whole of `google-sheet/Code.gs`, and press **Save**.
3. At the top, pick `testRow` and press **▶ Run**. Google asks you to allow access to your sheet: sign in and allow it (if it says "Google hasn't verified this app", press **Advanced → Go to … (unsafe)**; it's your own script). A test row appears in the Leads tab. Delete that row.
4. **Deploy → New deployment →** ⚙ **Web app.** Execute as: **Me**. Who has access: **Anyone**. Press **Deploy** and copy the **Web app URL** (it ends in `/exec`).
5. Send that link to Claude (or paste it into `SHEET` in `index.html`), then publish.

If you change `Code.gs` later: **Deploy → Manage deployments → ✏ → Version: New version → Deploy** (the link stays the same).

Only share the sheet with people who should see leads. The Web app link is visible in the page's code, but it can only add or update rows (each value is checked), never read them.

## The SME page (`sme/index.html`, for LinkedIn)

**Not live yet.** The SME page is kept on the local branch `sme-page` and left out of `main`, so publishing the checklist doesn't publish it. To publish it later, bring `sme/` into `main` as a new commit (don't push the `sme-page` branch itself: its history has private notes).

Built 25 Nov 2026 from the Instagram page, then translated and given its own content. Live since 25 Nov 2026. LinkedIn links (`?from=` or `?dari=` both work):

| Where | Link |
| --- | --- |
| Profile intro link | `https://check.saganproductions.com/sme/?from=linkedin-bio` |
| Featured section | `https://check.saganproductions.com/sme/?from=linkedin-featured` |
| First comment on a post | `https://check.saganproductions.com/sme/?from=linkedin-post` (or `?from=li-<post-name>`) |
| DM reply | `https://check.saganproductions.com/sme/?from=linkedin-dm` |

Ready-to-paste profile text is in `../linkedin-sme-links.md`.

- **Hero:** "If a key employee is out tomorrow, / What does your company actually cover?" with a drawing of a team holding up a "YOUR COMPANY" beam; one place is empty and circled as the GAP.
- **2 quick questions:** business type (Sdn Bhd / Partnership / Sole proprietor) and number of employees (1–5, 6–20, 21–50, 51+). The business type shows the one owner-succession point that fits (shareholders' agreement, partnership agreement, or personal liability). Before they choose, all three show (18 points; 16 after).
- **4 sections:** If an employee falls sick (5) · If an employee is injured or can't work again (4) · If a key person is gone (3) · If the owner is gone (4, of 6).
- **Form before the result:** name, company, mobile number, role (Owner / Director, HR / Admin, Other), consent tick.
- **WhatsApp message** is in English and includes company, role, business type and headcount.
- **Sheet:** SME leads go to their own tab, **SME Leads**, in the same Google Sheet (the script handles both pages; re-deploy the script after pasting the new `Code.gs`). The Dashboard tab only counts the Instagram leads for now.
- **Drawings:** `make_scenes.py` writes the SME drawings too.
- **Saved on the visitor's device** under its own key (`sme-audit-v1`), so the two pages don't mix.

**Facts and sources on the SME page (checked 25 Nov 2026 against the documents themselves unless noted):**
- Employment Act 1955 s.60F: 14–22 days sick leave, up to 60 days hospitalisation; employer pays for the examination; no duty in s.60F to pay hospital bills. Covers all wage levels since 1 Jan 2023 (JTKSM FAQ). Peninsular Malaysia and Labuan only.
- PERKESO: insured wage up to RM6,000 a month (contribution schedule). The percentage rates are not printed on the page because PERKESO's site blocked a direct check.
- PERKESO benefits: 80% of assumed daily wage, max RM158.67/day, MC of 4+ days; invalidity pension 50–65%, minimum RM550 (same sources as the Instagram page).
- LINDUNG 24 Jam (PERKESO FAQ, 13 Aug 2026): accidents outside working hours in Malaysia since 1 June 2026; mandatory for foreign workers and voluntary for local employees from 8 July 2026; 0.75% fully borne by the employee; no cover for disease unrelated to an accident. **Recheck before promoting:** the opt-out arrangement was reported to be under review.
- LHDN Public Ruling 11/2019 para 8.2.11: medical treatment benefit exempt. The page does not say a group medical contribution is tax-free for staff (Public Ruling 5/2019 para 6.8 treats some employer-paid premiums as a taxable perquisite); it says "confirm with your tax agent".
- LHDN Public Ruling 2/2003 (key-man insurance, 30 Dec 2003): deductible only for term life or accident policies payable to the company; not for shareholder-directors of a controlled company, partners or sole proprietors; proceeds taxable if the premium was allowed. The ruling speaks of insurance, not takaful, and is 23 years old; the page says to confirm with a tax agent.
- Partnership Act 1961 s.35 (not re-read by me; taken from the research report with its quote); Companies Act 2016 s.109; SSM comparison of business entities (unlimited liability); IFSA 2013 Schedule 10 (RM100,000); AIA (company medical benefits end with employment).
- Not used on the page but verified: DOSM "MSMEs Performance 2025" (released 30 July 2026): MSMEs were 48.7% of total employment in 2025, 8.09 million people.

**Before promoting the SME page:** AIA approval for this page too; a tax agent or AIA to confirm the two tax points; Sabah and Sarawak not covered (their own Labour Ordinances).

## Check before promoting

Compliance (BNM Policy Document on Product Transparency and Disclosure, 2 Dec 2024, paras 13.2–13.3; not legal advice):
- [ ] **Operator approval** covers this page. The checklist cards name no plans (examples say "satu pelan AIA PUBLIC Takaful"); plan names appear only in the source titles inside the pop-ups (A-Life Legasi Beyond page, A-Life Idaman PDS). The share button, reset link, plans list and bottom source list were removed.
- [x] **Title and agent code:** in the small print (`TITLE`, `CODE`).
- [x] **Registered name:** "Sagan" is the registered name (confirmed 24 Nov 2026), so `AGENT` stays empty and the page shows `NAME`.
- [ ] **PDPA (Personal Data Protection Act 2010):** the page now collects name, number, age, gender and checklist answers into your Google Sheet. The start form says what is collected, why, and that it isn't sold, and asks for consent to be contacted on WhatsApp. There is no line telling them how to ask for their data to be deleted (removed at your request); if someone asks, delete their row. Ask AIA whether agents may keep lead data in a personal Google Sheet, and whether they need a fuller privacy notice. Not legal advice; not verified.

Claims:
- [ ] **A-Plus WaiverExtra-i** is quoted from the A-Life Idaman PDS and has no page of its own on aia.com.my. Confirm it is still sold.
- [x] **LINDUNG 24 Jam** (changed 25 Nov 2026): the PERKESO item now says local employees can opt out (PERKESO FAQ, 13 Aug 2026). Recheck before promoting; the opt-out was reported to be under review.
- [ ] **Employment Act** text used is "as at 1 January 2023". Confirm 14/18/22 days and 60 days hospitalisation are unchanged. Sabah and Sarawak not checked.
- [ ] **"Tanpa rider macam ni, caruman tetap kena bayar walaupun gaji berhenti"**: general statement; true unless a plan has a waiver built in.
- [ ] **"Medical card bayar bil hospital, bukan gaji"** and **"Kad syarikat / perlindungan majikan ikut kerja"**: general statements; the page tells people to ask HR.
- [ ] **KWSP and PERKESO conditions** are summarised; the page says "ikut syarat".
- [ ] **"Saya balas satu-satu… Percuma"** and **"Korang yang buat keputusan"**: your own promises.
- [ ] Not tested on real phones (WhatsApp hand-off inside Instagram, Threads and TikTok on iOS and Android), and print not checked on paper.

## Files

- `index.html`: the whole page.
- `og.png`: the preview image shown when the link is shared (1200×630), white with the headline and the leaking GAJI bucket drawing.
- `sme/index.html`, `sme/og.png`: the LinkedIn page for SMEs and its link preview image.
- `CNAME`: the custom domain for GitHub Pages.
- `google-sheet/Code.gs`: the Google Apps Script that receives rows into your sheet (setup above). It contains nothing secret.
- `make_scenes.py`: draws the marker scenes with the carousel kit (`../carousels/engine/scenes.py`, same strokes and wobble as the reels) and writes them into `index.html` between `/*art*/` markers. Run `python3 make_scenes.py` after changing a drawing.

Preview locally: `python3 -m http.server 8765`, then open http://localhost:8765


WhatsApp quick replies for answering leads (one per checklist item, same facts and sources) are in `../whatsapp-quick-replies-checklist.md`, outside this folder so they are never published.


## Launch check (24 Nov 2026)

- Page: about 27 KB compressed; link preview 98 KB. Fonts trimmed: Inter about 48 KB on phones, the handwriting font about 9 KB (only the letters of the three notes).
- All 24 source pages respond; the 4 KWSP pages block automated checks (HTTP 403) but were read during research.
- WhatsApp message checked for: nothing ticked, everything settled, only "tak pasti"; name and age required before it opens.
- Fits a 320 px wide phone with no sideways scrolling. Print layout not checked.
- Still to do by Sagan: nothing on name or code (done), AIA approval for this page, one real-phone test from the Instagram bio.
