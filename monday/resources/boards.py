from typing import List, Optional
from monday.resources.base import BaseResource
from monday.query_joins import (
    get_boards_query,
    get_boards_by_id_query,
    get_board_items_query,
    get_columns_by_board_query,
    create_board_by_workspace_query,
    duplicate_board_query
)
from monday.resources.types import BoardKind, BoardState, BoardsOrderBy, DuplicateTypes


class BoardResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def fetch_boards(self, limit: int = None, page: int = None, ids: List[int] = None, board_kind: BoardKind = None, state: BoardState = None, order_by: BoardsOrderBy = None):
        query = get_boards_query(limit, page, ids, board_kind, state, order_by)
        return self.client.execute(query)

    def fetch_boards_by_id(self, board_ids):
        query = get_boards_by_id_query(board_ids)
        return self.client.execute(query)

    def fetch_items_by_board_id(self, board_ids, limit: Optional[int]=None, page: Optional[int]=None):
        query = get_board_items_query(board_ids, limit=limit, page=page)
        return self.client.execute(query)

    def fetch_columns_by_board_id(self, board_ids):
        query = get_columns_by_board_query(board_ids)
        return self.client.execute(query)

    def create_board(self, board_name: str, board_kind: BoardKind, workspace_id: int = None):
        query = create_board_by_workspace_query(board_name, board_kind, workspace_id)
        return self.client.execute(query)

    def duplicate_board(
        self,
        board_id: int,
        duplicate_type: DuplicateTypes,
        board_name: str = None,
        workspace_id: int = None,
        folder_id: int = None,
        keep_subscribers: bool = None,
    ):
        query = duplicate_board_query(board_id, duplicate_type, board_name, workspace_id, folder_id, keep_subscribers)
        return self.client.execute(query)
        return self.client.execute(query)
