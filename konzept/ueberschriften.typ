// #import "@preview/numbly:0.1.0": numbly

#let ueberschriften(doc) = [
  // #set heading(numbering: (..nums) => {
  //   let pos = nums.pos()
  //   if pos.len() == 1 {
  //     return numbering("I", ..nums)
  //   } else {
  //     return none
  //   }
  // })
  // #set heading(numbering: numbly(
  //   "{1:I}",
  //   none
  // ))
  
  #set heading(numbering: "1.1")
  #show heading.where(level: 2): h => [
    #v(1em)
    #h
    #v(0.5em)
  ]
  
  // #show heading.where(level: 1): h => [
  //   #pagebreak()
  //   #set text(font: "DejaVu Sans", size: 36pt)
  //   #align(center + horizon)[
  //     #counter(heading).display() \
  //     #h.body
  //   ]
  // ]
  // #show heading.where(level: 2): h => [
  //   #set text(font: "DejaVu Sans", size: 14pt)
  //   #h.body
  // ]
  #doc
]