const jalaali = require('jalaali-js')
const cc = new Date(622, 2, 22)
while (true) {
  const { jy, jm, jd } = jalaali.toJalaali(cc)
  if (jy === 3178) break
  console.log(`${cc.getFullYear()}-${cc.getMonth() + 1}-${cc.getDate()},${jy}-${jm}-${jd}`)
  cc.setDate(cc.getDate() + 1)
}
