module Update exposing (update)

import Command exposing (..)
import Date
import Types exposing (..)


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        SetDate date ->
            case date of
                Just d ->
                    let
                        year =
                            Date.year d
                    in
                        { model
                            | year = Just year
                            , current_year = year
                        }
                            ! [ getHolidays year ]

                Nothing ->
                    { model | year = Nothing } ! []

        ToggleYear ->
            case model.year of
                Nothing ->
                    model ! []

                Just year ->
                    if year == model.current_year then
                        let
                            year =
                                model.current_year + 1
                        in
                            { model | year = Just year } ! [ getHolidays year ]
                    else
                        { model | year = Just model.current_year }
                            ! [ getHolidays model.current_year ]

        HolidaysFetched (Ok new_model) ->
            { model
                | holidays = new_model.holidays
                , year = new_model.year
            }
                ! []

        HolidaysFetched (Err error) ->
            let
                _ =
                    Debug.log "Error" error
            in
                model ! []
