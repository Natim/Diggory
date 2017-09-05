module Types exposing (..)

import Date
import Time.Date
import Http


type alias Model =
    { holidays : List Holiday
    , year : Maybe Int
    }


type Msg
    = SetDate (Maybe Date.Date)
    | HolidaysFetched (Result Http.Error Model)


type alias Holiday =
    { date : Time.Date.Date
    , title : String
    , countries : List String
    }
