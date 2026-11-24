# Cek Perlindungan (free lead magnet)

One phone page that answers one question: **"Kalau esok jadi apa-apa, family korang boleh bertahan berapa lama?"**

Built like the good calculators out there:
- **Budget calculators** (NerdWallet, TransUnion 50/30/20): itemised lines, a running total and a "remaining" figure.
- **Life-cover calculators**: the DIME method (debt, income, mortgage, education, plus final costs), minus savings and existing cover, shown as needs vs have.

It is free to run: no backend, no database, no paid tools.

## The flow (6 steps, about 3 minutes)

1. **Tentang korang:** age, net salary, who depends on you (spouse / kids / parents / nobody). With kids, also the number of kids and the youngest's age.
2. **Belanja bulanan:** 8 lines.
   - Lines: house, car, food, transport, kids, bills, money for parents, other.
   - The live total shows "Lebihan" (left over) or "Terlebih" (overspent) against salary.
3. **Hutang:** remaining balances for house, car, personal, credit card, PTPTN and other. If there's a house loan, it asks about MRTT/MLTT.
4. **Simpanan & aset:** cash, investments (ASB, TH, unit trust), KWSP.
5. **Perlindungan:** own takaful/insurance, employer cover, a "tak pasti" box, and the medical card.
6. **Masa depan:**
   - years of support, on a slider
   - education fund per child
   - final and estate costs

## The result

- **Dark card:** "family boleh bertahan X tahun Y bulan" counts up on reveal, with a "% dilindungi" bar. For someone with no dependents it shows how long savings last without pay.
- **3 stats:** cover as a multiple of yearly salary, money left over each month, and months savings last without pay (or total debt for singles).
- **Duit family dari tahun ke tahun:** a chart of the family's money running down, with the shortfall in pink. The line under it tells the story, e.g. "Duit family habis lepas 11 tahun 4 bulan. Masa tu anak bongsu baru umur 14."
- **Cuba tambah perlindungan:** a slider plus a "Tutup gap penuh" button.
  - Moving it updates the big number, the chart, the bars and the gap live, so the visitor *sees* the fix.
  - If they use it, the WhatsApp message adds "Saya nak tahu pasal tambah perlindungan RMX".
- **Keperluan vs apa yang ada:** two stacked bars, each item listed, the gap shaded pink, a years-of-support stepper, and "Macam mana kiraan ni dibuat?" (the method).
- **Langkah seterusnya:** up to 4 personal next steps worked out from their numbers.
- **Bottom bar, always visible:** the gap + **"WhatsApp saya"**. It opens WhatsApp to you with everything typed out (their real numbers, not the slider's), plus "(dari: hibah)" when the link has `?dari=hibah`.
- **Simpan laporan (PDF):** prints a clean report (phone: Share → Save as PDF).
- **Share kalkulator ke pasangan.**

Each step's bottom bar also says what's still missing ("Isi gaji, siapa bergantung") instead of just greying out the button.

### The maths

```
Needs = support per month × 12 × years + debt + education (kids × amount) + final costs
Have  = savings + investments + KWSP + life cover (own + employer)
Gap   = Needs − Have
Bertahan (how long the family lasts) = (Have − debt − final costs) ÷ support per month
```

Support per month is worked out like this:
- With a spouse or kids: household spending, minus money for parents.
- With parents ticked: add the money you give them.
- If a house or car loan gets cleared, its monthly instalment is dropped too.
- A house loan with MRTT/MLTT is left out of debt.

Inflation and investment returns are not counted; the page says so.

## Go live (free)

1. Set `const WHATSAPP = "60XXXXXXXXX";` at the top of the `<script>` in `index.html`.
2. Host it on **GitHub Pages** (you're signed in as `visagannn`). It goes live at `https://visagannn.github.io/cek/`.
3. Point people to it:
   - link in bio
   - a story link sticker
   - **Meta Business Suite → Inbox → Automations → Comment to message**: free. Keywords are case-sensitive, so add `KIRA`, `kira`, `Kira`.
   - Skip the ManyChat free plan (reported cut to 25 contacts a month).

## Check before going live (editor brief: don't publish unverified claims)

- [ ] **Using "AIA TAKAFUL" on a public page:** ask your agency or compliance whether marketing tools need approval.
- [ ] **MRTT/MLTT explained as "Takaful yang lunaskan loan rumah kalau apa-apa jadi":** true only if it covers the full balance. The calculator treats "Ada" as fully covered.
- [ ] **A cleared house or car loan also removes its monthly instalment:** this is an assumption.
- [ ] **"KWSP tak dikira sebab biasanya tak boleh dikeluarkan serta-merta"** (in the no-pay scenario): check this, including the incapacitation withdrawal rules.
- [ ] **KWSP counted for the family after death:** it goes to the nominee; without one it takes longer.
- [ ] **Medical card from employer, "biasanya tamat" when you change jobs;** employer group life "biasanya hilang":
  - True for most group plans.
- [ ] **Default years (anak bongsu umur 23 / 5 tahun):** these are assumptions. Make sure you're comfortable defending them.
- [ ] **"Saya semak... percuma":** your own promise.

## Files

- `index.html`: the whole page.
- `make_scenes.py`: redraws the marker drawings (same strokes as the carousels) into the page.

Preview locally:

```
python3 -m http.server 8765 --directory lead-magnet
```

Then open http://localhost:8765
