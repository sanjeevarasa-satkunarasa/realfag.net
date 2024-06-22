function inputFileLocation() {
    return "eksamensoppgaver\Medie og Informasjonskunnskap 2\sam3009-medie-og-informasjonskunnskap-2-e-v23.pdf"
}

function outputFileLocation(fileLocation) {
    let output = fileLocation.replace("eksamensoppgaver","Eksamen ")
    output = output.split('/').join(' ')
    output = output.replace(".pdf", "")
    /*
    let output_array = output.split("")
    let yearIndex = 0
    for (let i = 0; i in output_array; i++){
      if (output_array[i] == "v" || output_array[i] == "h" && typeof output_array[i+1] === "number") {
        yearIndex = i
      } else if (output_array[i] == "V" || output_array[i] == "V" && typeof output_array[i+1] === "number"){
        yearIndex = i
      }
    }
  
    output = output_array.join("")
    */
    return output
}
