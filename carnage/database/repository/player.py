"""Module that represents the Player repository."""

from carnage.database.models.player import PlayerModel
from carnage.database.repository.base import BaseRepository


class PlayerRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(self, model: type[PlayerModel] = PlayerModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
