GROWX LEAD CATCHER - SPAM/SCRAPER GATE (Aug 30, 2026)
======================================================

WHAT CHANGED
------------
The lead endpoint (script.google.com/.../exec) was public with zero checks:
anyone who found the URL could POST fake leads straight into your "Growx
Leads" sheet and trigger the email notification, no site visit needed.

Code.gs now rejects a request unless:
  - it carries the right shared key (_k), which every real page on the
    site now sends automatically, and
  - its honeypot field (_hp) is empty, which only happens when a real
    person filled the form (a bot that blindly fills every input trips it)

A request that fails either check gets a quiet {"ok":true} back (so a bot
probing the endpoint learns nothing) and is never written to the sheet or
emailed.

Heads-up on what this is and isn't: the key lives in the site's own
JavaScript (assets/config.js), so it isn't secret from someone who
deliberately reads that file, it's not encryption. What it does is stop
the much larger and more common problem: generic bots and scraping
scripts that find the endpoint URL and fire blind POSTs at it without
ever loading the real page or its JS. That is the overwhelming majority
of junk this kind of endpoint gets.

THIS FILE (Code.gs) IS NOT LIVE UNTIL YOU DEPLOY IT
----------------------------------------------------
Same as the earlier fix in this folder: editing Code.gs here only changes
this local copy. The live endpoint keeps running whatever was last pasted
into the Apps Script editor and deployed there.

HOW TO APPLY (2 minutes)
-------------------------
1. Open the script editor:
   https://script.google.com/home/projects/1zrLXX3tvQcQTDcGZoYgxCRylh40GoMRfvrSl9f8yxWP87BWP2j93XAob/edit

2. Select everything in Code.gs (Ctrl+A) and paste the contents of the
   Code.gs in this folder over it. Save (Ctrl+S).

3. Deploy > Manage deployments > pencil (Edit) icon >
   Version: "New version" > Deploy.
   The /exec URL does not change, so nothing on the website needs updating.

4. Optional sanity check: pick "testLead" in the function dropdown and
   Run it. That call bypasses the gate (it calls save() directly, not
   doPost), so it will still write a row, that's expected and confirms
   the sheet itself still works.

Until step 3 is done, the site still works exactly as before (leads still
land in the sheet), the new fields (_k, _hp) will just show up as two
extra, harmless columns rather than being checked.

ALSO CHANGED ON THE SITE ITSELF (already live, no action needed)
------------------------------------------------------------------
Phone number is now a required field everywhere a lead is captured, not
optional:
  - Free-course certificate form (all 29 course pages): now asks for
    phone, not just name + email, validated before it will submit.
  - Charlie chat "raise a complaint" and "general enquiry" flows: used to
    accept "email or phone, either one", now asks for phone specifically
    (validated with a country code), with email as an optional follow-up.
  - Referral and job-application chat flows already required a validated
    phone number, unchanged.
