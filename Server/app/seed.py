'''This file is an initialization script, so that when the database tables are created for the first time, 
the restaurant menu is automatically persisted'''

from .models import Product
from .database import SessionLocal

# Function to insert the menu
def insert_initial_data():
    
    session = SessionLocal()
    
    # Checks if the menu has already been inserted
    if session.query(Product).count() == 0:
        
        # Restaurant menu, automatically inserted, when the first time the tables are initialized
        product_data = [
            ('Sushi de Caranguejo Picante', 'Imitação de carne de caranguejo com maionese picante envolta em nori e arroz de sushi.', 20.00, 'sushi', True),
            ('California Roll', 'Imitação de carne de caranguejo, abacate e pepino, enrolados em arroz de sushi e nori.', 18.00, 'sushi', False),
            ('Salmon and Avocado Roll', 'Salmão fresco e abacate, enrolados em nori e arroz de sushi.', 22.00, 'sushi', False),
            ('Mango Tiger Sushi Roll', 'Manga, abacate e kani enrolados em arroz de sushi e nori.', 24.00, 'sushi', False),
            ('Dynamite Roll', 'Tempura de camarão, pepino e abacate com molho picante.', 25.00, 'sushi', False),
            ('Rainbow Roll', 'Uma combinação colorida de peixes frescos e abacate.', 27.00, 'sushi', False),
            ('Spicy Tuna Roll', 'Atum picante com pepino e nori.', 23.00, 'sushi', False),
            ('Dragon Roll', 'Tempura de camarão, abacate e pepino com uma cobertura de enguia.', 28.00, 'sushi', False),
            ('Philadelphia Roll', 'Salmão, queijo creme e pepino.', 21.00, 'sushi', True),
            
            ('Classic Cheeseburger', 'Hambúrguer de carne bovina com queijo cheddar, alface, tomate e molho especial.', 28.00, 'hamburguer', False),
            ('BBQ Bacon Burger', 'Hambúrguer de carne bovina com queijo cheddar, bacon, cebola caramelizada e molho barbecue.', 32.00, 'hamburguer', True),
            ('Mushroom Swiss Burger', 'Hambúrguer de carne bovina com queijo suíço, cogumelos salteados e maionese.', 30.00, 'hamburguer', False),
            ('Spicy Jalapeño Burger', 'Hambúrguer de carne bovina com queijo pepper jack, jalapeños e maionese picante.', 29.00, 'hamburguer', False),
            ('Veggie Burger', 'Hambúrguer vegetariano com alface, tomate, cebola roxa e maionese.', 26.00, 'hamburguer', True),
            ('Blue Cheese Burger', 'Hambúrguer de carne bovina com queijo azul, cebola caramelizada e rúcula.', 33.00, 'hamburguer', False),
            ('Texas Burger', 'Hambúrguer de carne bovina com queijo cheddar, bacon, alface e molho barbecue.', 31.00, 'hamburguer', False),
            ('Hawaiian Burger', 'Hambúrguer de carne bovina com abacaxi grelhado, queijo suíço e molho teriyaki.', 34.00, 'hamburguer', False),
            ('Turkey Burger', 'Hambúrguer de peru com queijo suíço, alface e maionese.', 27.00, 'hamburguer', False),
            
            ('Mojito', 'Rum, hortelã, suco de limão, açúcar e água com gás.', 18.00, 'drinks', False),
            ('Caipirinha', 'Cachaça, limão, açúcar e gelo.', 16.00, 'drinks', True),
            ('Pina Colada', 'Rum, creme de coco e suco de abacaxi.', 20.00, 'drinks', False),
            ('Margarita', 'Tequila, suco de limão e licor de laranja.', 19.00, 'drinks', False),
            ('Mai Tai', 'Rum, suco de laranja, suco de abacaxi, grenadine e angostura.', 22.00, 'drinks', False),
            ('Cosmopolitan', 'Vodka, licor de laranja, suco de cranberry e suco de limão.', 21.00, 'drinks', False),
            ('Old Fashioned', 'Bourbon ou centeio, açúcar, Angostura e um toque de água.', 23.00, 'drinks', False),
            ('Manhattan', 'Whiskey, vermute doce e Angostura.', 24.00, 'drinks', True),
            ('Negroni', 'Gin, vermute doce e Campari.', 22.00, 'drinks', False),
            
            ('Spaghetti Carbonara', 'Espaguete com molho de ovo, queijo parmesão, pancetta e pimenta-do-reino.', 28.00, 'massas', True),
            ('Lasagna Bolognese', 'Lasanha com camadas de molho bolonhesa, bechamel e queijo.', 32.00, 'massas', True),
            ('Fettuccine Alfredo', 'Fettuccine com molho cremoso de queijo parmesão e manteiga.', 26.00, 'massas', False),
            ('Penne Arrabbiata', 'Penne com molho de tomate picante e manjericão.', 24.00, 'massas', False),
            ('Ravioli di Ricotta e Spinaci', 'Ravioli recheado com ricota e espinafre, servido com molho de tomate e manjericão.', 30.00, 'massas', False),
            ('Spaghetti Bolognese', 'Espaguete com molho bolonhesa e queijo parmesão.', 27.00, 'massas', False),
            ('Gnocchi al Pesto', 'Nhoque com molho pesto e parmesão.', 25.00, 'massas', False),
            ('Tagliatelle al Funghi', 'Tagliatelle com molho cremoso de cogumelos.', 29.00, 'massas', False),
            ('Linguine ai Frutti di Mare', 'Linguine com frutos do mar em molho de tomate.', 31.00, 'massas', False)
        ]

        # Iterates over the data and insert it into the 'product' table
        for name, description, price, category, isOnOffer in product_data:
            new_product = Product(name=name, description=description, price=price, category=category, isOnOffer=isOnOffer)
            session.add(new_product)

        # Commits Changes
        session.commit()
        # Closes Session
        session.close()