// const adarsh = ("adarsh")
// console.log(adarsh.trim(2,0))

// const adarshAge  = [1,2,3,7,5]
// console.log(adarshAge)

// const mohit = 36 /4 *(3+2)*4+2
// console.log(mohit)

// const praveen = 556

// if(praveen%2 == 0){
//     console.log("Yeas boi its even")
// } else {
//     console.log("Error its not even")
// }
// let number = 5;
// let factorial = 1;

// while (number>0) {
//     factorial = factorial * number
//     number = number - 1
// } console.log(factorial)

// let number = "Praveen"
// for (let sum = 0; sum < 100; sum++) {
//     console.log(number)
// } 

// let =  mohit = {
//     "NAME": "Mohit Kumar",
//     "AUID": "AGS19ABCA011",
//     "TYPE": "Student",
//     "Course": "BCA"
//   }  
// console.log(mohit.Course)
// function mohit() {
//     const mohit = {
//       "NAME": "Mohit Kumar",
//       "AUID": "AGS19ABCA011",
//       "TYPE": "Student",
//       "Course": "BCA"
//     } 
//     return  mohit.AUID
// }
// const userAuid = mohit()
// console.log(`Hey User your AUID is ${userAuid}`)

const express = require('express')
const request = require('request')
const cheerio = require('cheerio')
const axios = require('axios')
const app = express()
const port = 3001
const scrape = require('website-scraper')

axios({
  method: 'GET',
  url: 'https://randomword.com/',
  
}).then(function(response) {

  $ = cheerio.load(response.data);
  const data1 = $('#shared_section').text()
  return data1
} 

)

// app.use('/scrape', async(req,res) => {
//   var scrapedData = await scrapeData()
//   console.log(scrapedData)
//   res.send({
//     "Title" : scrapedData
//   })
// })

// async function scrapeData() {
//   request({
//     method: 'GET',
//     url: 'https://reqbin.com/'
//   },(err,req,res) => {
//     if(err) return console.error();
  
//     let $ = cheerio.load(res)
//     let title = $('title').text()
    
//     return title
//   })

// }



// async function loginAuth() {
//   var res = await axios.post('https://alive.university/api/v1/login/erp', {
//     "username": "AGS19ABCA072",
//     "password": "Ldxxxx2PA",
//     "usertype": "STUDENT",
//   }, {
//     headers: {
//         'Content-Type': 'application/json;charset=UTF-8',
//         "Access-Control-Allow-Origin": "*",
//         "Host": 'api.alive.university',
//         "Connection": 'keep-alive',
//         "Content-Length": '70',
//         "Accept": 'application/json, text/plain, /',
//         "User-Agent": 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
//         "Content-Type": 'application/json;charset=UTF-8',
//         "Origin": 'https://alive.university',
//         "Sec-Fetch-Site": 'same-site',
//         "Sec-Fetch-Mode": 'cors',
//         "Sec-Fetch-Dest": 'empty',
//         "Referer": 'https://alive.university/',
//         "Accept-Encoding": 'gzip, deflate, br',
//         "Accept-Language": 'en-US,en;q=0.9',
//     }
    
//   })
//   return res.data.token
// }



// app.use('/api', async (req, res) =>{
//   var loginVerify = await loginAuth()
//   // console.log(loginVerify)
//     res.send({
//       "Your Login Token" : loginVerify
//     })
// })

app.listen(port,()=>{
   console.log(`Your app is listening on ${port} port`) 
})
