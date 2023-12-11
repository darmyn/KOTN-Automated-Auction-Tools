from bot import scraper, parser
from enums import SortOrder, PageSize, AuctionCategory, ProductCategory

auction_content_filter = scraper.AuctionFilter(
    "TV",
    SortOrder.EndingSoon,
    AuctionCategory.All,
    PageSize.TwentyFive,
    ProductCategory.All
)

auction_content = scraper.fetch_auction_html(auction_content_filter, 1)

auction_data = 