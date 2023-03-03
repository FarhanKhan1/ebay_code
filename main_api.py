from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from launch import get_driver
import time
from selenium.webdriver.common.by import By
driver = get_driver()

app = Flask(__name__)
api = Api(app)
CORS(app)

class Nike(Resource):
    def get(self):
        pass
        # return {'message': 'This is the Nike endpoint'}
    def post(self):
        condition_id = 1000
        avg_sale_price_list = list()
        total_no_of_items_sold_list = list()
        style_list = list()
        data_ = request.get_json()
        day_range = data_["day_range"]
        condition = data_["condition"]
        if condition != "New":
            condition_id = 3000

        format = data_["format"]
        for style in data_["styles"]:    


            if len(style)>1:
                url_ = f"https://www.ebay.com/sh/research?marketplace=EBAY-US&keywords={style}&dayRange={day_range}&conditionId={condition_id}&format={format}"
                print(url_)
                # driver.get(url_)
                # time.sleep(5)
                # print("printing...")
                # avg_sold_price = driver.find_elements(By.CLASS_NAME, "metric-value")
                # print("getting avg sales price")
                # avg_sale_price_list.append(avg_sold_price[0].text)
                # style_list.append(style)
                # total_no_of_items_sold_list.append(avg_sold_price[4].text)
        # return {"style": style_list, "Avg Sold Price": avg_sale_price_list, "total_items_sold":total_no_of_items_sold_list}
        return    
class Ebay(Resource):
    def get(self):
        return {'message': 'This is the Ebay endpoint'}

    def post(self):
        count = -1
        condition_id = 1000
        avg_sale_price_list = list()
        total_no_of_items_sold_list = list()
        style_list = list()
        price_list = list()
        titles_list = list()
        profit_list = ["123"]
        ROI_list = ["456"]
        data_ = request.get_json()
        day_range = data_["day_range"]
        condition = data_["condition"]
        print(data_)
        if condition != "New":
            condition_id = 3000

        format = data_["format"]

        
        for style in data_["styles"]:
            count = count+1    
            try:
                if len(style)>1:
                    url_ = f"https://www.ebay.com/sh/research?marketplace=EBAY-US&keywords={style}&dayRange={day_range}&conditionId={condition_id}&format={format}"
                    # print(url_)
                    driver.get(url_)
                    time.sleep(1)
                    print("printing...")
                    avg_sold_price = driver.find_elements(By.CLASS_NAME, "metric-value")
                    print("getting avg sales price")
                    avg_sale_price_list.append(avg_sold_price[0].text)
                    style_list.append(style)
                    total_no_of_items_sold_list.append(avg_sold_price[4].text)
                    price_list.append(data_["price"][count])
                    titles_list.append(data_["title"][count])
                    print(avg_sale_price_list)
                    print(style_list)
                    print(total_no_of_items_sold_list)
                    print(price_list)
                    print(titles_list)
                    
            except Exception as e:
                print("ERROR: ", e)        
        return {"total_items":len(total_no_of_items_sold_list), "Profit": profit_list, "ROI": ROI_list, "Style": style_list, "Total_no_items_sold": total_no_of_items_sold_list, "Avg_Sold_Price": avg_sale_price_list , "Title":titles_list, "Price":price_list}
        # return {"avg sold price": avg_sold_price[0].text, "total_no_of_sold_items": avg_sold_price[4].text}


api.add_resource(Nike, '/nike')
api.add_resource(Ebay, '/ebay')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)