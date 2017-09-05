module Init exposing (..)

import Date
import Task
import Types exposing (..)


init : ( Model, Cmd Msg )
init =
    { holidays = []
    , year = Nothing
    , current_year = 0
    }
        ! [ now ]


now : Cmd Msg
now =
    Task.perform (Just >> SetDate) Date.now
