const cc = new Date(622, 2, 22)
const intl = new Intl.DateTimeFormat('fa-IR-u-nu-latn', {
  year: 'numeric',
  month: 'numeric',
  day: 'numeric',
  timeZone: 'GMT'
})

while (true) {
  const [ jy, jm, jd ] = intl.format(cc).split('/').map(v => parseInt(v))
  if (jy === 3178) break
  console.log(`${cc.getFullYear()}-${cc.getMonth() + 1}-${cc.getDate()},${jy}-${jm}-${jd}`)
  cc.setDate(cc.getDate() + 1)
}