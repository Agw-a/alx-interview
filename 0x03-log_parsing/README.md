## Description
Script that reads `stdin` line by line and computes metrics:

---

**Requirements**
- Inpit Format:
    - `<IP Address> - [<date] GET /projects/260 HTTP/1.1" <status code> <file size>`
-  After every 10 lines and/or a keyboard interruption `(CTRL + C)`, print these statistics from the beginning:
   -  Total file size: File size: `<total size>`. Total size is the sum of all previous `<file size>`
- Status code:
  - `200, 301, 400, 401, 403, 404, 405 and 500`
  - If a code is not an integer or doesn't appear donyt print anything.
  - format: `<status code>: <number>` printed in ascending order.