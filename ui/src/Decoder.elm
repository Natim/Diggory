module Decoder exposing (..)

import Array
import Json.Decode exposing (..)
import Json.Decode.Pipeline exposing (..)
import Time.Date as Date exposing (Date, date)
import Types exposing (..)


holidayDecoder : Decoder Holiday
holidayDecoder =
    decode Holiday
        |> required "date" decodeDate
        |> required "title" string
        |> required "countries" (list string)


holidaysDecoder : Decoder Model
holidaysDecoder =
    decode Model
        |> required "holidays" (list holidayDecoder)
        |> optional "year" (map Just int) Nothing


decodeDate : Decoder Date
decodeDate =
    string
        |> andThen
            (\value ->
                let
                    parts =
                        Array.fromList <|
                            String.split "-" value
                in
                    case ( Array.get 0 parts, Array.get 1 parts, Array.get 2 parts ) of
                        ( Just year, Just month, Just day ) ->
                            case ( String.toInt year, String.toInt month, String.toInt day ) of
                                ( Ok year, Ok month, Ok day ) ->
                                    succeed <| date year month day

                                _ ->
                                    fail <| "Unknown date: " ++ value

                        _ ->
                            fail <| "Unknown date: " ++ value
            )
