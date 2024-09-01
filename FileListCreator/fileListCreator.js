import fs from "fs";

filepath = "html\VG1.html";

const fs = require('fs')
fs.readFile(filepath, (err, output) => {
   if (err) throw err;
      console.log(output.toString());
});


