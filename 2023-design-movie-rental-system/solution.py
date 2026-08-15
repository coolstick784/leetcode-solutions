import heapq
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = {}
        self.unrented = {}
        self.prices = {}
        self.rented = []
        self.s_unrented = set()
        self.s_rented = set()
        for shop, movie, price in entries:
            self.movies.setdefault(movie, set()).add(shop)
            self.s_unrented.add((price, shop, movie))
            heapq.heappush(self.unrented.setdefault(movie, []), (price, shop, movie))
            self.prices[(movie, shop)] = price


    def search(self, movie: int) -> List[int]:
        cur = movie
        added = set()
        add_back = set()
        
        while self.unrented.get(movie) and len(added) < 5:
            price, shop, movie = heapq.heappop(self.unrented[movie])
            
            
            add_back.add((price, shop, movie))
            if shop not in self.movies[movie]:
                continue
            if movie != cur:
                continue
            added.add((price, shop, movie))
        added = sorted(list(added))
    
        out = [shop for price, shop, movie in added]
        for price, shop, movie in add_back:
            heapq.heappush(self.unrented[movie], (price, shop, movie))
        return out
        
        

    def rent(self, shop: int, movie: int) -> None:
        self.movies[movie].remove(shop)
        price = self.prices[(movie, shop)]
        self.s_unrented.remove((price, shop, movie))
        self.s_rented.add((price, shop, movie))
        heapq.heappush(self.rented, (price, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        self.movies[movie].add(shop)
        price = self.prices[(movie, shop)]
        
        if (price, shop, movie) not in self.s_unrented:
            self.s_unrented.add((price, shop, movie))
            self.s_rented.remove((price, shop, movie))

            heapq.heappush(self.unrented[movie], (price, shop, movie))
        

    def report(self) -> List[List[int]]:
        add_back = set()
        added = set()
        
        while self.rented and len(added) < 5:
            price, shop, movie = heapq.heappop(self.rented)
            if (price, shop, movie) not in self.s_rented:
                continue
            add_back.add((price, shop, movie))
            if shop in self.movies[movie]:
                continue
            
            added.add((price, shop, movie))
        added = sorted(list(added))
    
        out = [[shop, movie] for price, shop, movie in added]
        for price, shop, movie in add_back:
            heapq.heappush(self.rented, (price, shop, movie))
        return out
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
