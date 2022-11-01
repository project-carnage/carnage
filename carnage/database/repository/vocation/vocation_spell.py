from typing import Type

from sqlalchemy import select

from carnage.database.models.vocation import VocationSpellModel
from carnage.database.repository.base import BaseRepository


class VocationSpellRepository(BaseRepository):
    def __init__(
        self,
        model: Type[VocationSpellModel] = VocationSpellModel,
    ) -> None:
        super().__init__(model)

    def select_by_spell_id(self, spell_id: str) -> VocationSpellModel:
        statement = select(self.model).where(self.model.spell_id == spell_id)

        with self.session() as session:
            return session.execute(statement=statement).first()