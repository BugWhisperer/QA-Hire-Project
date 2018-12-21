# GET method tests

```
GIVEN I am a coach
AND I am not authorized to log into Hudl.com
WHEN I GET /Schedule URL to view a list of schedule entries
THEN I get status code 401 - Unauthorized
```

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I GET /Schedule URL to view a list of schedule entries with the following data object for a team’s schedule entry already exists
{
gameId: "1234567",
sqlId: "1234567",
date: "2016-01-01T19:00:00",
opponent: "TestOpponent",
opponentId: "123456",
isHome: true,
gameType: 0,
categories: [ ]
}
THEN I get status code 200 - OK
AND I get valid response headers: Contet-Type application/json
AND I get response body as valid JSON
AND I get JSON data gameId equal to "1234567"
AND I get JSON data sqlId equal to "1234567"
AND I get JSON data date equal to "2016-01-01T19:00:00"
AND I get JSON data opponent equal to "TestOpponent"
AND I get JSON data opponentId equal to "123456"
AND I get JSON data isHome is  true
AND I get JSON data gameType equal to 0
AND I get JSON data categories equal to  [ ]
```
# PUT method tests

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I PUT /Schedule/1234568 URL to update non-existing single schedule entry as below
{
gameId: "1234568",
sqlId: "1234567",
date: "2019-09-09T08:00:00",
opponent: "UpdatedTestOpponent",
opponentId: "123457",
isHome: false,
gameType: 1,
categories: [ “blah” ]
}
THEN I get status code 404 - Not Found
AND I get valid response headers: Contet-Type application/json
AND I get JSON response body as empty
```

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I PUT /Schedule/1234567 URL to update an existing single schedule entry as below
{
gameId: "1234567",
sqlId: "1234567",
date: "2019-09-09T08:00:00",
opponent: "UpdatedTestOpponent",
opponentId: "123457",
isHome: false,
gameType: 1,
categories: [ “blah” ]
}
THEN I get status code 200 - OK
AND I get valid response headers: Contet-Type application/json
AND I get response body as valid JSON
AND I get JSON data gameId equal to "1234567"
AND I get JSON data sqlId equal to "1234567"
AND I get JSON data date equal to "2019-09-09T08:00:00"
AND I get JSON data opponent equal to " UpdatedTestOpponent "
AND I get JSON data opponentId equal to "123457"
AND I get JSON data isHome is  false
AND I get JSON data gameType equal to 1
AND I get JSON data categories equal to  [ “blah” ]
```

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I PUT /Schedule/1234567 URL to update an existing single schedule entry as below
{
gameId: "1234567",
sqlId: "1234567",
date: "2019-09-09T08:00:00",
opponent: "UpdatedTestOpponent",
opponentId: "123457",
isHome: false,
gameType: 1,
categories: [ “blah” ]
}
THEN I get status code 200 - OK
AND I get valid response headers: Contet-Type application/json
AND I get response body as valid JSON
AND I get JSON data gameId equal to "1234567"
AND I get JSON data sqlId equal to "1234567"
AND I get JSON data date equal to "2019-09-09T08:00:00"
AND I get JSON data opponent equal to " UpdatedTestOpponent "
AND I get JSON data opponentId equal to "123457"
AND I get JSON data isHome is  false
AND I get JSON data gameType equal to 1
AND I get JSON data categories equal to  [ “blah” ]
```

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I GET /Schedule URL to view a list of schedule entries
THEN I get status code 200 - OK
AND I get valid response headers: Contet-Type application/json
AND I get response body as valid JSON
AND I get JSON data gameId equal to "1234567"
AND I get JSON data sqlId equal to "1234567"
AND I get JSON data date equal to "2019-09-09T08:00:00"
AND I get JSON data opponent equal to " UpdatedTestOpponent "
AND I get JSON data opponentId equal to "123457"
AND I get JSON data isHome is  false
AND I get JSON data gameType equal to 1
AND I get JSON data categories equal to  [ “blah” ]
```
# POST method tests

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I POST /Schedule URL to create a new schedule entry as below
{
gameId: "1234568",
sqlId: "1234567",
date: "2020-10-10T10:10:10",
opponent: "NewTestOpponent",
opponentId: "123458",
isHome: false,
gameType: 2,
categories: [ “blah2” ]
}
THEN I get status code 200 - Created
AND I get valid response headers: Contet-Type application/json
AND I get response body as valid JSON
AND I get JSON data gameId equal to "1234568"
AND I get JSON data sqlId equal to "1234567"
AND I get JSON data date equal to "2020-10-10T10:10:10"
AND I get JSON data opponent equal to " NewTestOpponent "
AND I get JSON data opponentId equal to "123458"
AND I get JSON data isHome is  false
AND I get JSON data gameType equal to 2
AND I get JSON data categories equal to  [ “blah2” ]
```

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I POST /Schedule URL to create a new schedule entry as below
{
gameId: "1234568",
sqlId: "1234567",
date: "2020-10-10T10:10:10",
opponent: "NewTestOpponent",
opponentId: "123458",
isHome: false,
gameType: 2,
categories: [ “blah2” ]
}
THEN I get status code 500 – Internal Server Error
AND I get valid error response indicating duplicate Id
GET after post to check new data saved
```

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I GET /Schedule URL to view a list of schedule entries
THEN I get status code 200 - OK
AND I get valid response headers: Contet-Type application/json
AND I get response body as valid JSON
AND I get JSON data gameId equal to "1234567"
AND I get JSON data sqlId equal to "1234567"
AND I get JSON data date equal to "2019-09-09T08:00:00"
AND I get JSON data opponent equal to " UpdatedTestOpponent "
AND I get JSON data opponentId equal to "123457"
AND I get JSON data isHome is  false
AND I get JSON data gameType equal to 1
AND I get JSON data categories equal to  [ “blah” ]
AND I also get JSON data gameId equal to "1234568"
AND I get JSON data sqlId equal to "1234567"
AND I get JSON data date equal to "2020-10-10T10:10:10"
AND I get JSON data opponent equal to " NewTestOpponent "
AND I get JSON data opponentId equal to "123458"
AND I get JSON data isHome is  false
AND I get JSON data gameType equal to 2
AND I get JSON data categories equal to  [ “blah2” ]
```

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I POST /Schedule URL to create a new schedule entry as below
{
gameId: BADREQUEST,
sqlId: "1234567",
date: "2020-10-10T10:10:10",
opponent: "NewTestOpponent",
opponentId: "123458",
isHome: false,
gameType: 2,
categories: [ “blah2” ]
}

THEN I get status code 400 – Bad Request
AND I get valid error response
```
# Delete method tests

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I DELETE /Schedule/1234567 URL to delete an existing single schedule entry
THEN I get status code 204 - OK
AND no data object is returned
```

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I DELETE /Schedule/1234567 URL to delete an existing single schedule entry
THEN I get status code 404 – Not Found
``` 

```
GIVEN I am a coach
AND I am authorized to log into Hudl.com
WHEN I GET /Schedule URL to view a list of schedule entries
THEN I get status code 200 - OK
AND I get valid response headers: Contet-Type application/json
AND I get response body as valid JSON
AND I also get JSON data gameId equal to "1234568"
AND I get JSON data sqlId equal to "1234567"
AND I get JSON data date equal to "2020-10-10T10:10:10"
AND I get JSON data opponent equal to " NewTestOpponent "
AND I get JSON data opponentId equal to "123458"
AND I get JSON data isHome is  false
AND I get JSON data gameType equal to 2
AND I get JSON data categories equal to  [ “blah2” ]
```