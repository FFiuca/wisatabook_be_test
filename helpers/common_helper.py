def paginate_model(page, limit=10):
    offset = (page-1)* limit
    next_row = page* limit

    return [offset, next_row]
