module Types exposing (..)

import Date
import Time.Date
import Http


type alias Holidays =
    { holidays : List Holiday
    , year : Maybe Int
    }


type alias Model =
    { holidays : List Holiday
    , year : Maybe Int
    , current_year : Int
    }


type Msg
    = SetDate (Maybe Date.Date)
    | HolidaysFetched (Result Http.Error Holidays)
    | ToggleYear


type alias Holiday =
    { date : Time.Date.Date
    , title : String
    , countries : List String
    }
