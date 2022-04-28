/**
 * 脚本 替换对比网址
 * 2022/04/29
 * write by
 * https://github.com/liulinboyi
 */
const fs = require('fs')
const path = require('path')

let content = fs.readFileSync(path.resolve(__dirname, '../index.html')).toString()

/** 正则替换对比网址 */
function replacer(match, p1, p2, offset, string) {
    let palce = match.replace(p1, '`http://${location.host}/compare`')
    return palce
}

content.replace(/await[\s]+postData\((.+?)(\s*,\s*[\s\S]+)*\)/, replacer)

fs.writeFileSync(path.resolve(__dirname, '../templates/compare.html'), content)