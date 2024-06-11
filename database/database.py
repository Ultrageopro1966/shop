"""Supabase client."""

from __future__ import annotations

from supabase import Client, create_client


class SupabaseClient:
    """Supabase client."""

    def __init__(self: SupabaseClient, url: str, key: str) -> None:
        """Init supabase client."""
        self.__url = url
        self.__key = key
        self.__client: Client = create_client(self.__url, self.__key)

    def get_password(self: SupabaseClient, login: str) -> str | None:
        """Get password."""
        response = (
            self.__client.table("users").select("password").eq("login", login).execute()
        )
        return response.data[0].get("password") if response.data else None

    def new_user(self: SupabaseClient, login: str, password: str) -> bool:
        """Create new user."""
        try:
            self.__client.table("users").insert(
                {"login": login, "password": password},
            ).execute()
        except Exception:  # noqa: BLE001
            return False
        else:
            return True

    def get_user(self: SupabaseClient, login: str) -> dict[str, str] | None:
        """Get user."""
        response = self.__client.table("users").select("*").eq("login", login).execute()
        return response.data[0] if response.data else None

    def get_coins(self: SupabaseClient, login: str) -> int | None:
        """Get coins."""
        response = (
            self.__client.table("users").select("coins").eq("login", login).execute()
        )
        return response.data[0].get("coins") if response.data else None

    def add_coins(self: SupabaseClient, login: str, new_coins: int) -> bool:
        """Add coins."""
        coins = self.get_coins(login)
        if coins is None:
            return False

        self.__client.table("users").update({"coins": coins + new_coins}).eq(
            "login",
            login,
        ).execute()

        return True
