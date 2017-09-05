module View exposing (view)

import Time.Date as Date exposing (Date)
import Html exposing (..)
import Html.Attributes exposing (..)
import Types exposing (..)


view : Model -> Html Msg
view model =
    div [ class "container-fluid" ]
        [ headerView model
        , mainView model
        ]


mainView : Model -> Html Msg
mainView model =
    div [ class "row" ]
        [ div [ class "col-sm-12" ]
            [ case model.year of
                Nothing ->
                    spinner

                Just year ->
                    displayHolidays year model.holidays
            ]
        ]


headerView : Model -> Html Msg
headerView model =
    nav
        [ class "navbar navbar-default" ]
        [ div
            [ class "container-fluid" ]
            [ div
                [ class "navbar-header" ]
                [ a [ class "navbar-brand", href "#" ] [ text "Mozilla Global Public Holidays" ] ]
            ]
        ]


spinner : Html Msg
spinner =
    div [ class "loader" ] []


displayHolidays : Int -> List Holiday -> Html Msg
displayHolidays year holidays =
    div []
        [ h2 []
            [ strong [] [ text <| toString year ]
            , displayHolidaysPerMonth holidays |> div [ class "container-fluid" ]
            ]
        ]


displayHolidaysPerMonth : List Holiday -> List (Html Msg)
displayHolidaysPerMonth holidays =
    [ div [ class "row" ]
        [ displayMonth "January" 1 holidays
        , displayMonth "February" 2 holidays
        , displayMonth "March" 3 holidays
        , displayMonth "April" 4 holidays
        ]
    , div [ class "row" ]
        [ displayMonth "May" 5 holidays
        , displayMonth "June" 6 holidays
        , displayMonth "July" 7 holidays
        , displayMonth "August" 8 holidays
        ]
    , div [ class "row" ]
        [ displayMonth "September" 9 holidays
        , displayMonth "October" 10 holidays
        , displayMonth "November" 11 holidays
        , displayMonth "December" 12 holidays
        ]
    ]


displayMonth : String -> Int -> List Holiday -> Html Msg
displayMonth name month holidays =
    div [ class "col-md-3" ]
        [ h2 [] [ text name ]
        , filterMonth month holidays
            |> List.map displayHoliday
            |> ul []
        ]


filterMonth : Int -> List Holiday -> List Holiday
filterMonth month holidays =
    List.filter (\h -> month == (Date.month h.date)) holidays


displayHoliday : Holiday -> Html Msg
displayHoliday holiday =
    li []
        [ strong [] [ text <| displayDate holiday.date ]
        , text " : "
        , a [ href "#", title <| String.join ", " holiday.countries ] [ text holiday.title ]
        ]


displayDate : Date -> String
displayDate date =
    (toString <| Date.day date)
