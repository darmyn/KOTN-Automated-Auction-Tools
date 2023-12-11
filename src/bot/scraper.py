import requests
from requests.models import Response
from enums import SortOrder, AuctionCategory, PageSize, ProductCategory
from config import urls

class AuctionFilter:
    def __init__(
            self,
            searchQuery: str = "",
            sortOrder = SortOrder.EndingSoon,
            auctionCategory = AuctionCategory.All,
            pageSize = PageSize.TwentyFive,
            productCategory: ProductCategory = ProductCategory.All
        ):
        self.SearchQuery = searchQuery
        self.SortOrder = sortOrder
        self.AuctionCategory = auctionCategory
        self.PageSize = pageSize
        self.ProductCategory = productCategory

def _is_request_success(result: Response):          
    if result.status_code == 200:
        return True
    else:
        return False 

def fetch_html(self, url: str):
    response = requests.get(url)
    if _is_request_success(response):
        return response.content
        
def fetch_home_html():
    return fetch_html(urls.BASE_URL)

def fetch_login_html():
    return fetch_html(urls.LOGIN_URL)
        
def fetch_auction_html(
    self,
    auctionFilter: AuctionFilter, 
    page: int = 1,
):
    path = f"{auctionFilter.AuctionCategory}"
    query = f"""
        ?category={auctionFilter.AuctionCategory}
        &order_by={auctionFilter.SortOrder}
        &per_page={auctionFilter.PageSize}
        &page={str(page)}
        &find={auctionFilter.SearchQuery}
    """
    final_url = f"{urls.BASE_URL}/{path}/{query}"
    return self.fetch_html(final_url)