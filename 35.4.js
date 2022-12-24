const verif=(word)=>{
  var s=0
  var l=word.length

  for(let i=0 ; i<=l;i++) {
    if (word[i]=="o") {
      s++
    }
  }
  if (s>=2) {
    return true
  } else {
    return false
  }
}