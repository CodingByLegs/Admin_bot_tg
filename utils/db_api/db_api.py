from asyncpg import Connection
from asyncpg.exceptions import UniqueViolationError
from loader import db


class DBCommands:
    pool: Connection = db
    GET_PRODUCT_IS_SELL_FROM_CATEGORY_LIST = 'SELECT name.name_of_product, name.id' \
                                             'FROM public."Name of product" AS name' \
                                             'LEFT JOIN public."Is sell" AS s ON name.id = s.id' \
                                             'LEFT JOIN public."Tip" as tip ON name.id = tip.id' \
                                             "WHERE s.is_sell = true AND tip.type = '$1'"

    GET_PRODUCT_IS_STOCK_FROM_CATEGORY_LIST = 'SELECT name.name_of_product, name.id' \
                                              'FROM public."Name of product" AS name' \
                                              'LEFT JOIN public."Item status" AS stat ON name.id = stat.id' \
                                              'LEFT JOIN public."Tip" AS tip ON name.id = tip.id' \
                                              "WHERE stat.item_status = 0 AND tip.type = '$1'"

    GET_CATEGORY_LIST = 'SELECT DISTINCT(t.type) AS Unic_types FROM public."Tip" AS t'

    DELETE_RECORD = 'DELETE FROM public."Name of product" as name WHERE name.id = $1;'

    GET_NAME_OF_PRODUCT = 'SELECT name_of_product FROM public."Name of product" AS name WHERE name.id = $1'

    GET_COST_PRICE = 'SELECT cost_price FROM public."Cost price" AS cost WHERE cost.id = $1'

    GET_COST_DELIVERY = 'SELECT cost_delivery FROM public."Cost delivery" AS del_cost WHERE del_cost.id = $1'

    GET_SELLING_PRICE = 'SELECT selling_price FROM public."Selling price" AS sel_price WHERE sel_price.id = $1'

    GET_PRODUCT_MARGIN = 'SELECT product_margin FROM public."Margin_product" AS margin WHERE margin.id = $1'

    GET_DISCOUNT = 'SELECT discount FROM public."Discount" AS disc WHERE disc.id = $1'

    GET_IS_SELL = 'SELECT isSell FROM public."Is sell" AS is_sell WHERE is_sell.id = $1'

    GET_SIZE_OF_PRODUCT = 'SELECT size_of_product FROM public."Size of product" AS size WHERE size.id = $1'

    GET_STATE = 'SELECT state FROM public."State" AS state WHERE state.id = $1'

    GET_TYPE = 'SELECT type FROM public."Tip" AS tip WHERE tip.id = $1'

    GET_COLOR = 'SELECT color FROM public."Color" AS color WHERE color.id = $1'

    GET_DATE_IN = 'SELECT date_in FROM public."Date in" AS date_in WHERE date_in.id = $1'

    GET_DATE_OUT = 'SELECT date_out FROM public."Date out" AS date_out WHERE date_out.id = $1'

    GET_TOTAL_PRICE = 'SELECT total_price FROM public."Total price" AS total WHERE total.id = $1'

    GET_EXTRA_HOURS = 'SELECT extra_hours FROM public."Extra hours" AS extra WHERE extra.id = $1'

    GET_INV_EXPENSES = 'SELECT inv_expenses FROM public."Invested expenses" AS inv WHERE inv.id = $1'

    GET_DELIVERY_METHOD = 'SELECT delivery_method FROM public."Delivery method" AS del_method WHERE del_method.id = $1'

    GET_PROFIT = 'SELECT profit FROM public."Profit" AS profit WHERE profit.id = $1'

    GET_ITEM_STATUS = 'SELECT item_status FROM public."Item status" AS status WHERE status.id = $1'

    GET_PHOTO = 'SELECT photo FROM public."Photo" AS photo WHERE photo.id = $1'

    GET_QR_ID = 'SELECT QR_id FROM public."QR_id" AS qr WHERE qr.id = $1'

    SET_NAME_OF_PRODUCT = 'UPDATE public."Name of product" SET name_of_product = $1 WHERE id = $2;'

    SET_COST_PRICE = 'UPDATE public."Cost price" SET cost_price = $1 WHERE id = $2'

    SET_COST_DELIVERY = 'UPDATE public."Cost delivery" SET cost_delivery = $1 WHERE id = $2'

    SET_SELLING_PRICE = 'UPDATE public."Selling price" SET selling_price = $1 WHERE id = $2'

    SET_DISCOUNT = 'UPDATE public."Discount" SET discount = $1 WHERE id = $2'

    SET_IS_SELL = 'UPDATE public."Is sell" SET isSell = $1 WHERE id = $2'

    SET_SIZE_OF_PRODUCT = 'UPDATE public."Size of product" SET size_of_product = $1 WHERE id = $2'

    SET_STATE = 'UPDATE public."State" SET state = $1 WHERE id = $2'

    SET_TYPE = 'UPDATE public."Tip" SET type = $1 WHERE id = $2'

    SET_COLOR = 'UPDATE public."Color" SET color = $1 WHERE id = $2'

    SET_DATE_IN = 'UPDATE public."Date in" SET date_in = $1 WHERE id = $2'

    SET_DATE_OUT = 'UPDATE public."Date out" SET date_out = $1 WHERE id = $2'

    SET_TOTAL_PRICE = 'UPDATE public."Total price" SET total_price = $1 WHERE id = $2'

    SET_EXTRA_HOURS = 'UPDATE public."Extra hours" SET extra_hours = $1 WHERE id = $2'

    SET_INV_EXPENSES = 'UPDATE public."Invested expenses" SET inv_expenses = $1 WHERE id = $2'

    SET_DELIVERY_METHOD = 'UPDATE public."Delivery method" SET delivery_method = $1 WHERE id = $2'

    SET_ITEM_STATUS = 'UPDATE public."Item status" SET item_status = $1 WHERE id = $2'

    SET_PHOTO = 'UPDATE public."Photo" SET photo = $1 WHERE id = $2'

    SET_QR_ID = 'UPDATE public."QR_id" SET QR_id = $1 WHERE id = $2'

    SET_MARGIN_PRODUCT = 'UPDATE public."Margin_product" SET product_margin = $1 WHERE id = $2'

    SET_PROFIT = 'UPDATE public."Profit" SET profit = $1 WHERE id = $2'

    ADD_NAME_OF_PRODUCT = 'INSERT INTO public."Name of product" (name_of_product, id) VALUES ($1, $2);'

    ADD_COST_PRICE = 'INSERT INTO public."Cost price" (cost_price, id) VALUES ($1, $2);'

    ADD_COST_DELIVERY = 'INSERT INTO public."Cost delivery" (cost_delivery, id) VALUES ($1, $2)'

    ADD_SELLING_PRICE = 'INSERT INTO public."Selling price" (selling_price, id) VALUES ($1, $2)'

    ADD_DISCOUNT = 'INSERT INTO public."Discount" (discount, id) VALUES ($1, $2)'

    ADD_IS_SELL = 'INSERT INTO public."Is sell" (isSell, id) VALUES ($1, $2)'

    ADD_SIZE_OF_PRODUCT = 'INSERT INTO public."Size of product"(size_of_product, id) VALUES ($1, $2)'

    ADD_STATE = 'INSERT INTO public."State" (state, id) VALUES ($1, $2)'

    ADD_TYPE = 'INSERT INTO public."Tip" (type, id) VALUES ($1, $2)'

    ADD_COLOR = 'INSERT INTO public."Color" (color, id) VALUES ($1, $2)'

    ADD_DATE_IN = 'INSERT INTO public."Date in" (date_in, id) VALUES ($1, $2)'

    ADD_DATE_OUT = 'INSERT INTO public."Date out" (date_out, id) VALUES ($1, $2)'

    ADD_TOTAL_PRICE = 'INSERT INTO public."Total price" (total_price, id) VALUES ($1, $2)'

    ADD_EXTRA_HOURS = 'INSERT INTO public."Extra hours" (extra_hours, id) VALUES ($1, $2)'

    ADD_INV_EXPENSES = 'INSERT INTO public."Invested expenses" (inv_expenses, id) VALUES ($1, $2)'

    ADD_DELIVERY_METHOD = 'INSERT INTO public."Delivery method" (delivery_method, id) VALUES ($1, $2)'

    ADD_ITEM_STATUS = 'INSERT INTO public."Item status" (item_status, id) VALUES ($1, $2)'

    ADD_PHOTO = 'INSERT INTO public."Photo" (photo, id) VALUES ($1, $2)'

    ADD_QR_ID = 'INSERT INTO public."QR_id" (QR_id, id) VALUES ($1, $2)'

    ADD_PRODUCT_MARGIN = 'INSERT INTO public."Margin_product" (product_margin, id) VALUES ($1, $2)'

    ADD_PROFIT = 'INSERT INTO public."Profit" (profit, id) VALUES ($1, $2)'

    async def get_product_is_sell_from_category_list(self, type):
        return await self.pool.fetchval(self.GET_PRODUCT_IS_SELL_FROM_CATEGORY_LIST, type)

    async def get_product_is_stock_from_category_list(self, type):
        return await self.pool.fetchval(self.GET_PRODUCT_IS_STOCK_FROM_CATEGORY_LIST, type)

    async def get_category_list(self):
        return await self.pool.fetchval(self.GET_CATEGORY_LIST)

    async def delete_record(self, id):
        try:
            await self.pool.fetchval(self.DELETE_RECORD, id)
        except UniqueViolationError:
            pass

    async def get_name_of_product(self, id):
        return await self.pool.fetchval(self.GET_NAME_OF_PRODUCT, id)

    async def get_cost_price(self, id):
        return await self.pool.fetchval(self.GET_COST_PRICE, id)

    async def get_cost_delivery(self, id):
        return await self.pool.fetchval(self.GET_COST_DELIVERY, id)

    async def get_selling_price(self, id):
        return await self.pool.fetchval(self.GET_SELLING_PRICE, id)

    async def get_product_margin(self, id):
        return await self.pool.fetchval(self.GET_PRODUCT_MARGIN, id)

    async def get_discount(self, id):
        return await self.pool.fetchval(self.GET_DISCOUNT, id)

    async def get_isSell(self, id):
        return await self.pool.fetchval(self.GET_IS_SELL, id)

    async def get_size_of_product(self, id):
        return await self.pool.fetchval(self.GET_SIZE_OF_PRODUCT, id)

    async def get_state(self, id):
        return await self.pool.fetchval(self.GET_STATE, id)

    async def get_type(self, id):
        return await self.pool.fetchval(self.GET_TYPE, id)

    async def get_color(self, id):
        return await self.pool.fetchval(self.GET_COLOR, id)

    async def get_date_in(self, id):
        return await self.pool.fetchval(self.GET_DATE_IN, id)

    async def get_date_out(self, id):
        return await self.pool.fetchval(self.GET_DATE_OUT, id)

    async def get_total_price(self, id):
        return await self.pool.fetchval(self.GET_TOTAL_PRICE, id)

    async def get_extra_hours(self, id):
        return await self.pool.fetchval(self.GET_EXTRA_HOURS, id)

    async def get_inv_expenses(self, id):
        return await self.pool.fetchval(self.GET_INV_EXPENSES, id)

    async def get_delivery_method(self, id):
        return await self.pool.fetchval(self.GET_DELIVERY_METHOD, id)

    async def get_profit(self, id):
        return await self.pool.fetchval(self.GET_PROFIT, id)

    async def get_item_status(self, id):
        return await self.pool.fetchval(self.GET_ITEM_STATUS, id)

    async def get_photo(self, id):
        return await self.pool.fetchval(self.GET_PHOTO, id)

    async def get_QR_id(self, id):
        return await self.pool.fetchval(self.GET_QR_ID, id)

    async def set_name_of_product(self, id, name):
        args = name, id
        try:
            await self.pool.fetchval(self.SET_NAME_OF_PRODUCT, *args)
        except UniqueViolationError:
            pass

    async def set_cost_price(self, id, price):
        args = price, id
        try:
            await self.pool.fetchval(self.SET_COST_PRICE, *args)
        except UniqueViolationError:
            pass

    async def set_cost_delivery(self, id, del_cost):
        args = del_cost, id
        try:
            await self.pool.fetchval(self.SET_COST_DELIVERY, *args)
        except UniqueViolationError:
            pass

    async def set_selling_price(self, id, price):
        args = price, id
        try:
            await self.pool.fetchval(self.SET_SELLING_PRICE, *args)
        except UniqueViolationError:
            pass

    async def set_discount(self, id, disc):
        args = disc, id
        try:
            await self.pool.fetchval(self.SET_DISCOUNT, *args)
        except UniqueViolationError:
            pass

    async def set_isSell(self, id, issell):
        args = issell, id
        try:
            await self.pool.fetchval(self.SET_IS_SELL, *args)
        except UniqueViolationError:
            pass

    async def set_size_of_product(self, id, size):
        args = size, id
        try:
            await self.pool.fetchval(self.SET_SIZE_OF_PRODUCT, *args)
        except UniqueViolationError:
            pass

    async def set_state(self, id, state):
        args = state, id
        try:
            await self.pool.fetchval(self.SET_NAME_OF_PRODUCT, *args)
        except UniqueViolationError:
            pass

    async def set_type(self, id, type):
        args = type, id
        try:
            await self.pool.fetchval(self.SET_TYPE, *args)
        except UniqueViolationError:
            pass

    async def set_color(self, id, color):
        args = color, id
        try:
            await self.pool.fetchval(self.SET_COLOR, *args)
        except UniqueViolationError:
            pass

    async def set_date_in(self, id, date_in):
        args = date_in, id
        try:
            await self.pool.fetchval(self.SET_DATE_IN, *args)
        except UniqueViolationError:
            pass

    async def set_date_out(self, id, date_out):
        args = date_out, id
        try:
            await self.pool.fetchval(self.SET_DATE_OUT, *args)
        except UniqueViolationError:
            pass

    async def set_total_price(self, id, price):
        args = price, id
        try:
            await self.pool.fetchval(self.SET_TOTAL_PRICE, *args)
        except UniqueViolationError:
            pass

    async def set_extra_hours(self, id, extra):
        args = extra, id
        try:
            await self.pool.fetchval(self.SET_EXTRA_HOURS, *args)
        except UniqueViolationError:
            pass

    async def set_inv_expenses(self, id, inv):
        args = inv, id
        try:
            await self.pool.fetchval(self.SET_INV_EXPENSES, *args)
        except UniqueViolationError:
            pass

    async def set_delivery_method(self, id, method):
        args = method, id
        try:
            await self.pool.fetchval(self.SET_DELIVERY_METHOD, *args)
        except UniqueViolationError:
            pass

    async def set_item_status(self, id, status):
        args = status, id
        try:
            await self.pool.fetchval(self.SET_ITEM_STATUS, *args)
        except UniqueViolationError:
            pass

    async def set_photo(self, id, photo):
        args = photo, id
        try:
            await self.pool.fetchval(self.SET_PHOTO, *args)
        except UniqueViolationError:
            pass

    async def set_QR_id(self, id, qr):
        args = qr, id
        try:
            await self.pool.fetchval(self.SET_QR_ID, *args)
        except UniqueViolationError:
            pass

    async def add_product(self, id, name_of_product, cost_price, date_in, type, item_status,
                          selling_price=0, discount=None,  isSell=False, size_of_product=None, state=None, color=None,
                          date_out=None, total_price=None, extra_hours=None, inv_expenses=None, delivery_method=None,
                          photo=None, QR_id=None, cost_delivery=None):
        try:
            await self.pool.fetchval(self.ADD_NAME_OF_PRODUCT, [name_of_product, id])
            await self.pool.fetchval(self.ADD_COST_PRICE, [cost_price, id])
            await self.pool.fetchval(self.ADD_COST_DELIVERY, [cost_delivery, id])
            await self.pool.fetchval(self.ADD_DATE_IN, [date_in, id])
            await self.pool.fetchval(self.ADD_TYPE, [type, id])
            await self.pool.fetchval(self.ADD_ITEM_STATUS, [item_status, id])
            await self.pool.fetchval(self.ADD_SELLING_PRICE, [selling_price, id])
            await self.pool.fetchval(self.ADD_DISCOUNT, [discount, id])
            await self.pool.fetchval(self.ADD_IS_SELL, [isSell, id])
            await self.pool.fetchval(self.ADD_SIZE_OF_PRODUCT, [size_of_product, id])
            await self.pool.fetchval(self.ADD_STATE, [state, id])
            await self.pool.fetchval(self.ADD_COLOR, [color, id])
            await self.pool.fetchval(self.ADD_DATE_OUT, [date_out, id])
            await self.pool.fetchval(self.ADD_TOTAL_PRICE, [total_price, id])
            await self.pool.fetchval(self.ADD_EXTRA_HOURS, [extra_hours, id])
            await self.pool.fetchval(self.ADD_INV_EXPENSES, [inv_expenses, id])
            await self.pool.fetchval(self.ADD_DELIVERY_METHOD, [delivery_method, id])
            await self.pool.fetchval(self.ADD_PHOTO, [photo, id])
            await self.pool.fetchval(self.ADD_SELLING_PRICE, [selling_price, id])
            await self.pool.fetchval(self.ADD_QR_ID, [QR_id, id])
            await self.pool.fetchval(self.ADD_PRODUCT_MARGIN, [0, id])
            await self.pool.fetchval(self.ADD_PROFIT, [0, id])
        except UniqueViolationError:
            pass

    async def set_margin(self, id):
        cp: int = await self.get_cost_price(id)
        cd: int = await self.get_cost_delivery(id)
        sp: int = await self.get_selling_price(id)
        disc: int = await self.get_discount(id)
        if cd is not None and disc is not None:
            marga = (((cp + cd)/(sp - disc))-100)*100
            profit = sp - (cp + cd + disc)
        elif cd is None and disc is not None:
            marga = ((cp / (sp - disc)) - 100) * 100
            profit = sp - (cp + disc)
        elif cd is not None and disc is None:
            marga = (((cp + cd)/sp)-100)*100
            profit = sp - (cp + cd)
        else:
            marga = ((cp/sp)-100)*100
            profit = sp - cp
        try:
            await self.pool.fetchval(self.SET_MARGIN_PRODUCT, [marga, id])
            await self.pool.fetchval(self.SET_PROFIT, [profit, id])
        except UniqueViolationError:
            pass


db = DBCommands()
