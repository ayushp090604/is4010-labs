import argparse
import os
import sys

FAVORITES_FILE = "favorites.json"

from week08.favorites import FavoritesManager
from week08.weather_api import (
    WeatherAPI,
    format_current_weather,
    format_forecast
)


def load_api_key():
    key = os.getenv("WEATHER_API_KEY")

    if key:
        return key

    try:
        import config
        return config.WEATHER_API_KEY
    except (ImportError, AttributeError):
        return None


def build_parser():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    current = subparsers.add_parser("current")
    current.add_argument("location")

    forecast = subparsers.add_parser("forecast")
    forecast.add_argument("location")
    forecast.add_argument(
        "--days",
        type=int,
        default=3
    )

    favorites = subparsers.add_parser("favorites")
    fav_sub = favorites.add_subparsers(
    dest="favorites_command"
)

    add = fav_sub.add_parser("add")
    add.add_argument("name")
    add.add_argument("location")

    remove = fav_sub.add_parser("remove")
    remove.add_argument("name")

    fav_sub.add_parser("list")

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    favorites = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":

        if args.favorites_command == "add":
            if not favorites.add(args.name, args.location):
                print(
                    "Favorite already exists",
                    file=sys.stderr
                )
                return 1

            return 0

        if args.favorites_command == "remove":
            if not favorites.remove(args.name):
                print(
                    "Favorite not found",
                    file=sys.stderr
                )
                return 1

            return 0

        if args.favorites_command == "list":
            for name, location in favorites.list_all().items():
                print(f"{name}: {location}")

            return 0

    api_key = load_api_key()

    if not api_key:
        print(
            "Missing API key",
            file=sys.stderr
        )
        return 1

    api = WeatherAPI(api_key)

    if args.command == "current":

        location = (
            favorites.get_location(args.location)
            or args.location
        )

        data = api.get_current_weather(location)

        if data is None:
            print(
                "Request failed",
                file=sys.stderr
            )
            return 1

        print(format_current_weather(data))
        return 0

    if args.command == "forecast":

        location = (
            favorites.get_location(args.location)
            or args.location
        )

        try:
            data = api.get_forecast(
                location,
                args.days
            )
        except ValueError as e:
            print(str(e), file=sys.stderr)
            return 1

        if data is None:
            print(
                "Request failed",
                file=sys.stderr
            )
            return 1

        print(format_forecast(data))
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())