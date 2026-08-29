GROWX LEAD CATCHER - FIX
========================

PROBLEM FOUND
-------------
Apps Script Executions log shows:

    Version 1 | doPost | Web App | Aug 27, 2026, 9:53:39 PM | 0.831 s | FAILED
    Version 1 | doGet  | Web App | Aug 27, 2026, 9:51:22 PM | 0.988 s | Completed

So the test lead DID reach the script, but doPost crashed and nothing was written
to the sheet. Cause: the script used

    SpreadsheetApp.getActiveSpreadsheet()

This is a STANDALONE script project, not bound to the "Growx Leads" sheet, so
getActiveSpreadsheet() returns null and the call throws.

THE FIX
-------
Code.gs (in this folder) opens the sheet explicitly:

    SpreadsheetApp.openById('1c875Kxk7VxrlPOCYEWsEkTmRZbL9fzf_OBPlv4r1gFw')

It also now:
  - creates the header row automatically on first run
  - adds a new column automatically for any field the site sends that
    is not in the header yet (so nothing is ever silently dropped)
  - returns {"ok":false,"error":"..."} instead of a blank 500 on failure
  - sends the email notification inside its own try/catch, so a mail
    quota problem can never lose the row

HOW TO APPLY (5 steps, ~2 minutes)
----------------------------------
1. Open the script editor:
   https://script.google.com/home/projects/1zrLXX3tvQcQTDcGZoYgxCRylh40GoMRfvrSl9f8yxWP87BWP2j93XAob/edit

2. Select everything in Code.gs (Ctrl+A) and paste the contents of the
   attached Code.gs over it. Save (Ctrl+S).

3. Pick "testLead" in the function dropdown at the top and click Run.
   It should say "Execution completed" and put one row in the sheet.

4. Deploy > Manage deployments > pencil (Edit) icon >
   Version: "New version" > Deploy.
   IMPORTANT: this step is what makes the live site use the new code.
   The /exec URL does NOT change, so nothing on the website needs updating.

5. Tell me and I will fire a real test lead from the live site to confirm
   end to end.

CLEANUP
-------
Once it works, delete the test rows ("editor-test" and "test-from-claude")
from the sheet.
