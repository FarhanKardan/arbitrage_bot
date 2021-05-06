 class Algorithem():
    def __init__(self, orderbook):
        self.orderbook = orderbook
        self.exchanges = ['Bw', 'Hit', 'Digifinex', 'Kucoin']

    '''Calculating the profit in each arbitrage opportunity'''

    def profit_calculator(self, f_exchange, first_price, first_vol, s_exchange, second_price, second_vol):
        # different exchange fees
        exchange_fees = {'Bw': 0.1, 'Kucoin': 0.1, 'Hit': 0.1, 'Digifinex': 0.20}
        # Finding the highest possibale volume
        vol = min(first_vol, second_vol)
        # taker Calculator
        taker_fee = ((vol * first_price) / 100) * exchange_fees[f_exchange]
        buy = (vol * first_price) - round(taker_fee, 2)
        # maker Calculator
        maker_fee = ((vol * second_price) / 100) * exchange_fees[s_exchange]
        sell = (vol * second_price) - round(maker_fee, 2)
        # Profit calculator
        profit = round(sell - buy, 2)
        return profit, vol

    ''' pulling ask_vals '''
    def ask_vals(self, name):
        ask_price = float(self.orderbook[name]['asks'][0][0])
        ask_vol = float(self.orderbook[name]['asks'][0][1])
        return ask_price, ask_vol

    ''' Pulling bid vals '''
    def bid_vals(self, name):
        bid_price = float(self.orderbook[name]['bids'][0][0])
        bid_vol = float(self.orderbook[name]['bids'][0][1])
        return bid_price, bid_vol

    ''' finding arbitrage opportunites across the different exchanges'''
    def arb_opp(self, threshold, vol_limit, limit_exchange=False):
        '''threshold : minmium amount of profit size'''
        global best_opp
        '''vol_limit : maximum amount of the volume in a transaction '''
        '''limit_exchane: find opportunites exspet that exchange'''
        # Creating a list of all exchnages permutation
        perm = list(permutations(self.exchanges, 2))
        best_profit = 0
        for exchange in perm:
            # define the first and second exchanges
            f_exchange, s_exchange = (exchange[0]), (exchange[1])
            # Pulling orderbook data
            ask_price, ask_vol = ask_vals(orders, f_exchange)
            bid_price, bid_vol = bid_vals(orders, s_exchange)
            # Calculating the profit for two exchanges
            if ask_price < bid_price:
                profit, vol = profit_calculator(f_exchange, ask_price, ask_vol, s_exchange, bid_price, bid_vol)
                # Find all acctable arbitrages
                if best_profit >= threshold and vol <= vol_limit and profit > best_profit:
                    # getting the highest profit arbitrage
                    best_profit = profit
                    best_opp = (f_exchange, ask_price, s_exchange, bid_price, vol, best_profit)
            return best_opp
