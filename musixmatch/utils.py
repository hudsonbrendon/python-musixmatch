def _set_page_size(page_size):
    if page_size > 100:
        page_size = 100
    elif page_size < 1:
        page_size = 1
    return page_size
