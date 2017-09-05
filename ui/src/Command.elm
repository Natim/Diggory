module Command exposing (..)

import Decoder exposing (..)
import Http
import HttpBuilder exposing (..)
import Time
import Types exposing (..)


getHolidays : Int -> Cmd Msg
getHolidays year =
    HttpBuilder.get ("https://diggory.dev.mozaws.net/v0/holidays/" ++ (toString year))
        |> withTimeout (10 * Time.second)
        |> withExpect (Http.expectJson holidaysDecoder)
        |> send HolidaysFetched
