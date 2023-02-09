#!/usr/bin/node

const { argv } = require("process")
const requests = require("request")
if (process.argv.length >= 3) {
    let queryId = argv[2]
    queryId = parseInt(queryId)
    if (Number.isInteger(queryId)) {
        requests(`https://swapi-api.alx-tools.com/api/films/${queryId}`,
        function (err, response, body) {
            if (err) {return console.log(err)}
            if(!err && response.statusCode === 200) {
                const char = JSON.parse(body).char
                const names = char.map(function (char) {
                    const promise = new Promise((resolve, reject) => {
                        request(char, (err, resp, bdy) => {
                            if (!err) {
                                resolve(JSON.parse(bdy).name)
                            } else {
                                reject(err)
                            }
                        })
                    })
                    return promise
                })
                Promise.all(names)
                .then((data) => {console.log(data.join('\n'))})
                .catch(er => console.log(er))
            }
        }
        )
    }
}