import os
import openai
from thefuzz import fuzz, process
from dotenv import load_dotenv

 

class InventoryAssistant:
    def __init__(self):
        load_dotenv()
        Api_key = os.getenv("OPEN_API_KEY")        
        self.client = openai.OpenAI(api_key=Api_key)
        self.numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']
        self.productos = [
    "Coca-Cola Regular", "Coca-Cola Sin Azúcar", "Pepsi Regular", "Pepsi Black", "Sabritas Clásicas",
    "Sabritas Adobadas", "Sabritas Limón", "Doritos Nacho", "Doritos Flaming Hot", "Cheetos Bolita",
    "Cheetos Torciditos", "Ruffles Original", "Ruffles Queso", "Takis Fuego", "Takis Nitro",
    "Barcel Chips", "Barcel Mix", "Barcel Churritos", "Ricolino Bubulubu", "Ricolino Paleta Payaso",
    "Ricolino Kranky", "Ricolino Lunetas", "Ricolino Duvalín", "Marinela Gansito", "Marinela Pingüinos",
    "Marinela Choco Roles", "Marinela Submarinos", "Marinela Pinguinos de Fresa", "Bimbo Pan Blanco",
    "Bimbo Pan Integral", "Bimbo Conchas", "Bimbo Mantecadas", "Bimbo Roles de Canela", "Wonder Pan Integral",
    "Wonder Pan Blanco", "Ruffles Mega Crunch", "Gamesa Emperador Chocolate", "Gamesa Emperador Limón",
    "Gamesa Chokis", "Gamesa Marias", "Gamesa Saladitas", "Oreo Clásicas", "Oreo Golden", "Oreo Mini",
    "Nescafé Clásico", "Nescafé Decaf", "Nescafé Dolca", "Nescafé Gold", "La Costeña Chiles Jalapeños",
    "La Costeña Frijoles Refritos", "La Costeña Salsas", "La Costeña Chiles en Escabeche", "Herdez Salsa Casera",
    "Herdez Salsa Verde", "Herdez Guacamole", "McCormick Mayonesa", "McCormick Mostaza", "McCormick Catsup",
    "Barcel Takis Xplosion", "Pepsi Manzana", "Ciel Agua Natural", "Bonafont Agua Natural", "Jumex Néctar de Mango",
    "Jumex Néctar de Durazno", "Jumex Néctar de Manzana", "Del Valle Jugo de Naranja", "Del Valle Néctar de Manzana",
    "Del Valle Frutopia", "Nutrileche Leche Entera", "Nutrileche Leche Deslactosada", "Santa Clara Leche Deslactosada",
    "Lala Yogur Natural", "Lala Yogur de Fresa", "Danone Activia Natural", "Danone Danonino", "Danone Yoplait Griego",
    "Danone Vitalínea", "Nestlé Nido", "Nestlé Svelty", "Nestlé La Lechera", "Nestlé Carnation Clavel",
    "Abuelita Chocolate en Polvo", "Hershey's Chocolate en Polvo", "Choco Milk Polvo", "Gerber Papilla de Manzana",
    "Gerber Papilla de Plátano", "Suero Oral Pedialyte", "Electrolit Naranja", "Gatorade Azul", "Gatorade Uva",
    "Powerade Azul", "Powerade Naranja", "Halls Mentol", "Halls Sandía", "Trident Menta", "Trident Fresa",
    "Lala Queso Panela", "Lala Queso Oaxaca", "Philadelphia Queso Crema", "Santa Clara Crema Natural",
    "Nutella", "Skippy Crema de Cacahuate", "Maruchan Ramen de Pollo", "Maruchan Ramen de Camarón",
    "Knorr Suiza Caldo de Pollo","La Moderna Pasta de Coditos", "La Moderna Pasta de Espagueti", "Maseca Harina de Maíz",
    "Tres Estrellas Harina de Trigo", "Minsa Harina de Maíz", "Gamesa Galletas Marias", "Gamesa Canelitas",
    "Gamesa Mamut", "Quaker Avena", "Karo Miel de Maíz", "Ajumex Pulparindo", "Ajumex Rellerindos", "Pulparindo Mini",
    "Mazapán De La Rosa", "Marinela Sponch", "Marinela Chocotorro", "Marinela Gansito", "Coca-Cola Light",
    "Sprite Sin Azúcar", "Fanta Naranja", "Fanta Fresa", "Dr. Pepper", "Canada Dry Ginger Ale",
    "Topo Chico Agua Mineral", "Agua Electrolit Coco",
    "Agua Electrolit Fresa", "Yoli Refresco de Limón", "Manzanita Sol", "Lala Lala Milkshake", "Santa Clara Crema",
    "Santa Clara Yogur Natural", "Santa Clara Yogur Fresa", "Zucaritas de Kellogg's", "Corn Flakes de Kellogg's",
    "All Bran de Kellogg's", "Honey Nut Cheerios", "Trix de General Mills", "Choco Krispis de Kellogg's",
    "Nestlé Crunch", "KitKat", "Carlos V", "Carlos V Blanco", "Toblerone", "Ferrero Rocher", "M&M's",
    "M&M's Peanut", "Snickers", "Milky Way", "Twix", "Bubulubu", "Pulparindo", "Skwinkles", "Salsaguetis",
    "Rockaleta", "Canel's Chicle", "Trident Sin Azúcar", "Orbit", "Coca-Cola Zero", "Fresca Cítrica",
    "Sidral Mundet", "Ciel Mineralizada", "Bonafont Kids", "Bonafont Levite Limón", "Jumex Antiox",
    "Del Valle Néctar Durazno", "Cheetos Poffs", "Fritos Sabritas", "Crujitos", "Picafresas",
    "Chocoretas", "Oreo Red Velvet", "Gamesa Animalitos", "Gamesa Bombones", "Gamesa Saladitas",
    "Marinela Twinkie", "Herdez Guacamole Salsa", "Herdez Salsa Verde Casera", "Herdez Salsa Roja Casera",
    "Bimbo Mantecadas", "Bimbo Negrito", "Bimbo Cuernitos", "Bimbo Roles", "Bimbo Chocolatín",
    "Gamesa Florentinas", "Gamesa Empanadas de Piña", "Nutrileche Leche Light", "Nestlé Nescafé Decaf",
    "Nestlé Nescafé Cappuccino", "Lala Yogur Frutos Rojos", "Philadelphia Dip", "Danone Activia Ciruela",
    "Danone Yoplait Griego Natural", "Danone Yoplait Griego Mango", "Santa Clara Nieve Vainilla",
    "Santa Clara Nieve Chocolate", "Santa Clara Paleta Chocolate", "Bubulubu Minis", "Duvalín Choco-Vainilla", "La Costeña Chiles Chipotles", "La Costeña Chiles Serranos", "La Costeña Frijoles Bayos", "Herdez Chipotles",
    "Herdez Jalapeños", "McCormick Ajo en Polvo", "McCormick Orégano", "McCormick Pimienta Negra", "Herdez Alcaparras",
    "Del Fuerte Puré de Tomate", "Del Fuerte Salsa de Tomate", "Knorr Suiza Caldo de Verduras", "Knorr Suiza Caldo de Res",
    "Knorr Pasta Espagueti", "Doña María Mole Poblano", "Doña María Mole Verde", "Sazonador Maggi", "Rexal Polvo para Hornear",
    "Royal Polvo para Hornear", "Tres Estrellas Masa para Tamal", "Tres Estrellas Panque de Vainilla", "San Marcos Jalapeños",
    "San Marcos Frijoles Refritos", "Bachoco Muslo de Pollo", "Bachoco Pechuga de Pollo", "Pilgrim's Alas de Pollo",
    "Pilgrim's Pierna de Pollo", "Capullo Aceite de Canola", "Nutrioli Aceite de Maíz", "Carbonell Aceite de Oliva",
    "La Fina Sal", "Sabormex Sal", "Ibarra Chocolate de Mesa", "Abuelita Chocolate de Mesa", "Alpura Crema Natural",
    "Alpura Leche Entera", "Alpura Leche Deslactosada", "Nestlé La Lechera Condensada", "Nestlé Leche Evaporada",
    "Santa Clara Crema Natural", "Bonafont Water Levite", "Bonafont Agua Natural", "Ciel Agua Natural",
    "Salsa Valentina Negra", "Salsa Valentina Roja", "La Morena Jalapeños", "La Morena Chipotle", "La Morena Salsa", "Cheetos Flaming Hot", "Cheetos Bolita", "Doritos Nacho", "Doritos Flamin' Hot", "Doritos Pizzerola", "Doritos Dinamita",
    "Sabritas Original", "Sabritas Adobadas", "Sabritas Limón", "Ruffles Queso", "Ruffles Mega Crunch", "Ruffles Flamin' Hot",
    "Takis Fuego", "Takis Xplosion", "Takis Nitro", "Takis Zombie", "Fritos Original", "Fritos Chorizo y Chipotle",
    "Crujitos", "Crujitos Flamin' Hot", "Churrumais", "Churrumais Limón", "Chicharrones Barcel", "Chicharrones Del Rancho",
    "Chicharrones Pica Limón", "Tostitos Original", "Tostitos Salsa Verde", "Tostitos Flamin' Hot", "Tostitos Guacamole",
    "Tostitos con Queso", "Tostitos con Chile", "Cacahuates Hot Nuts Original", "Hot Nuts Flamin' Hot",
    "Cacahuates De La Rosa", "Cacahuates Japonés Nishikawa", "Cacahuates con Chile Mafer", "Papas Chips Churrumaiz",
    "Cacahuates Mafer Salados", "Kranky Ricolino", "Bubulubu Ricolino", "Paleta Payaso Ricolino", "Panditas Ricolino",
    "Rockaleta", "Vero Mango", "Vero Elote", "Skwinkles Salsagheti", "Skwinkles Rellenos", "Pulparindo Tamarindo",
    "Pulparindo Mango", "Rellerindos", "Salsaguetis", "Lucas Muecas", "Lucas Gusano", "Lucas Chamoy",
    "Pelón Pelo Rico", "Pelón Pelo Rico Chamoy", "Chamoy Miguelito", "Miguelito Polvo", "Chaca Chaca",
    "Gomitas de Ositos Haribo", "Gomitas de Moritas Haribo", "Gomitas de Fresas Haribo", "Gomitas de Frutas Osito",
    "Gomitas de Frutas Miguelito", "Panditas Enchilados", "Picafresas", "Picafresas Enchiladas", "Choco Krispis Barritas",
    "Chocoretas", "Panditas Trululu", "Palomitas ACT II Mantequilla", "Palomitas ACT II Queso", "Palomitas ACT II Natural",
    "Palomitas PopCine", "Palomitas Slim Pop", "Tostitos Tiras", "Tostitos Limón", "Tostitos Queso Nacho",
    "Pringles Original", "Pringles Queso", "Pringles Cebolla", "Pringles Jalapeño", "Pringles Flamin' Hot",
    "Cheetos Poffs", "Doritos Diablo", "Papitas Sabritas de Chile y Limón", "Papitas Barcel Churritos",
    "Sabritas Adobadas Grandes", "Sabritones Barcel", "Churritos de Maíz Hot", "Sabritones Limón",
    "Palomitas Barcel Banchos", "Palomitas Barcel Bravitas", "Palomitas Barcel Con Queso", "Churrumais Asado",
    "Doritos Taco", "Takis Intensos", "Takis Nitro Limón", "Takis Crunchy Fajita", "Takis Churritos de Fuego",
    "Cacahuates Japoneses Hot Nuts", "Cacahuates con Limón Hot Nuts", "Cacahuates Enchilados Hot Nuts",
    "Bubulubu Minis", "Skwinkles Chamoy", "Salsagheti de Tamarindo", "Paletas de Chile Rocaleta", "Pulparindots", "Tequila José Cuervo Tradicional", "Tequila José Cuervo Especial", "Tequila Don Julio Blanco",
    "Tequila Don Julio Reposado", "Tequila Don Julio 70", "Tequila Herradura Plata", "Tequila Herradura Reposado",
    "Tequila Herradura Añejo", "Tequila Patrón Silver", "Tequila Patrón Reposado", "Tequila 1800 Blanco",
    "Tequila 1800 Reposado", "Tequila Clase Azul Reposado", "Tequila Clase Azul Añejo", "Tequila Casa Dragones Blanco",
    "Tequila Casa Dragones Joven", "Mezcal Montelobos Espadín", "Mezcal Montelobos Tobalá", "Mezcal Alipús San Andrés",
    "Mezcal Alipús San Baltazar", "Mezcal Ojo de Tigre", "Mezcal Los Amantes Reposado", "Mezcal Los Amantes Joven",
    "Mezcal Del Maguey Vida", "Mezcal Del Maguey Chichicapa", "Mezcal Del Maguey Crema de Mezcal", "Mezcal Bruxo No. 1",
    "Mezcal Bruxo No. 2", "Mezcal Unión Joven", "Mezcal Unión Viejo", "Mezcal Amores Espadín", "Mezcal Amores Cupreata",
    "Cerveza Corona Extra", "Cerveza Corona Light", "Cerveza Corona Familiar", "Cerveza Modelo Especial",
    "Cerveza Negra Modelo", "Cerveza Victoria", "Cerveza Pacífico", "Cerveza Pacífico Light", "Cerveza Sol Clásica",
    "Cerveza Sol Michelada", "Cerveza Indio", "Cerveza Indio Pilsner Plata", "Cerveza Dos Equis Lager",
    "Cerveza Dos Equis Ámbar", "Cerveza Tecate Light", "Cerveza Tecate Roja", "Cerveza Heineken",
    "Cerveza Bud Light", "Cerveza Michelob Ultra", "Whisky Chivas Regal 12", "Whisky Chivas Regal Extra",
    "Whisky Buchanan's 12", "Whisky Buchanan's Master", "Whisky Jack Daniel's Old No. 7", "Whisky Jack Daniel's Honey",
    "Whisky Johnnie Walker Red Label", "Whisky Johnnie Walker Black Label", "Whisky Ballantine's Finest",
    "Vodka Absolut Azul", "Vodka Absolut Citron", "Vodka Smirnoff No. 21", "Vodka Smirnoff Tamarindo",
    "Vodka Grey Goose", "Vodka Stolichnaya", "Vodka Belvedere", "Ron Bacardí Blanco", "Ron Bacardí Añejo",
    "Ron Bacardí Solera", "Ron Havana Club 3 Años", "Ron Havana Club Añejo 7 Años", "Ron Captain Morgan",
    "Ron Malibu Coco", "Brandy Presidente", "Brandy Torres 10", "Brandy Fundador", "Brandy Azteca de Oro",
    "Vino Tinto Casillero del Diablo Cabernet Sauvignon", "Vino Tinto Casillero del Diablo Merlot",
    "Vino Tinto Concha y Toro Reservado", "Vino Blanco Santa Carolina", "Vino Blanco Viña San Pedro",
    "Vino Espumoso Freixenet", "Vino Rosado Barefoot", "Vino Tinto Barefoot Merlot", "Vino Blanco Casa Madero",
    "Vino Tinto Casa Madero Merlot", "Vino Tinto L.A. Cetto Cabernet Sauvignon", "Vino Tinto L.A. Cetto Petite Sirah",
    "Vino Blanco L.A. Cetto Chardonnay", "Vino Blanco Monte Xanic", "Vino Rosado Monte Xanic", "Vino Espumoso Codorníu",
    "Licor de Café Kahlúa", "Licor de Hierbas Jägermeister", "Licor de Naranja Cointreau", "Licor de Crema Bailey's Original",
    "Licor de Menta Peppermint", "Anís Chinchón", "Anís del Mono", "Cognac Hennessy V.S", "Cognac Rémy Martin V.S.O.P.",
    "Cognac Martell Cordon Bleu", "Tequila Sauza Silver", "Tequila Sauza Gold", "Tequila Cazadores Blanco",
    "Tequila Cazadores Reposado", "Mezcal Espina Negra Espadín", "Mezcal Mezcaloteca Joven", "Tequila Milagro Silver", "Shampoo Pantene Reparación", "Shampoo Head & Shoulders Anticaspa", "Shampoo Sedal Brillo",
    "Shampoo Dove Hidratación", "Shampoo Herbal Essences Coco", "Acondicionador Pantene Restauración",
    "Acondicionador Dove Nutrición", "Acondicionador Head & Shoulders Suavidad", "Jabón Zest Aqua",
    "Jabón Palmolive Naturals", "Jabón Dove Original", "Jabón Escudo Antibacterial", "Jabón Protex Protección",
    "Jabón Líquido Palmolive Oliva", "Gel Antibacterial Kleenex", "Gel Antibacterial Escudo", "Crema Nivea Soft",
    "Crema Corporal Lubriderm", "Crema Corporal Jergens", "Crema Corporal Neutrogena", "Crema Corporal Dove",
    "Crema de Manos Nivea", "Crema de Manos Atrix", "Crema de Manos Palmolive", "Pasta Dental Colgate Triple Acción",
    "Pasta Dental Crest 3D White", "Pasta Dental Sensodyne", "Pasta Dental Colgate Máxima Protección",
    "Enjuague Bucal Listerine Cool Mint", "Enjuague Bucal Colgate Plax", "Enjuague Bucal Crest", 
    "Desodorante Axe Dark Temptation", "Desodorante Dove Invisible Dry", "Desodorante Nivea Men Black & White",
    "Desodorante Rexona Clinical", "Desodorante Lady Speed Stick", "Desodorante Speed Stick Power",
    "Crema para Afeitar Gillette", "Crema para Afeitar Nivea Men", "Crema para Afeitar Barbasol",
    "After Shave Gillette", "After Shave Nivea Men", "Espuma para Afeitar Gillette Sensitive",
    "Rastrillos Gillette Mach3", "Rastrillos Bic Flex3", "Rastrillos Wilkinson Sword", "Toallas Femeninas Kotex Nocturnas",
    "Toallas Femeninas Saba Buenas Noches", "Toallas Femeninas Always Ultra", "Tampones Tampax Regular",
    "Tampones Saba Compactos", "Protector Diario Kotex", "Protector Diario Always", "Protector Diario Saba",
    "Papel Higiénico Pétalo Rendimax", "Papel Higiénico Charmin Ultra", "Papel Higiénico Regio", 
    "Papel Higiénico Suavel", "Papel Higiénico Kleenex Cottonelle", "Paños Húmedos Huggies", 
    "Paños Húmedos Kleenex", "Paños Húmedos Cottonelle", "Cotonetes Johnson's", "Cotonetes Kleenex",
    "Cepillo de Dientes Colgate Extra Clean", "Cepillo de Dientes Oral-B Cuidado Completo", "Cepillo de Dientes Reach",
    "Cepillo de Dientes Colgate Sensitive", "Crema Depilatoria Veet", "Crema Depilatoria Nair", "Cera Depilatoria Veet",
    "Acondicionador Pantene Fuerza y Brillo", "Crema Ponds Clarant B3", "Crema Nivea Reafirmante", 
    "Crema Corporal Jergens Hidratante", "Crema Lubriderm Suavidad", "Bloqueador Solar Nivea Factor 50",
    "Bloqueador Solar Hawaiian Tropic", "Bloqueador Solar Banana Boat", "Bloqueador Solar Neutrogena",
    "Shampoo para Bebé Johnson's Baby", "Loción para Bebé Johnson's", "Jabón para Bebé Huggies",
    "Aceite para Bebé Johnson's", "Shampoo Head & Shoulders Mentol", "Shampoo Caprice Herbal", 
    "Gel Fijador Ego Wet Look", "Gel Fijador Moco de Gorila", "Spray para el Cabello Pantene", 
    "Spray para el Cabello Tresemmé", "Laca para el Cabello Elnett", "Enjuague Bucal Biorepair",
    "Desodorante Secret Powder Fresh", "Crema Antiarrugas L'Oréal Revitalift", "Crema Antiarrugas Olay Regenerist",
    "Gel Limpiador Facial Neutrogena", "Gel Limpiador Facial La Roche-Posay Effaclar", "Crema para Pies Neutrogena",
    "Crema para Pies Atrix", "Crema Corporal Dove Hidratación Profunda", "Protector Solar Bioderma Photoderm",
    "Protector Solar La Roche-Posay Anthelios", "Protector Solar Avène Cleanance"
]
        
    def parse_instruction(self, instruction):
            # Llama al modelo de OpenAI para interpretar la instrucción
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages = [
                    {
                        "role": "system",
                        "content": (
                            "You are an inventory management assistant. Answer only in the format requested, without adding any extra information. "
                            "I will provide a list of products so that you create the correct format without mistakes in recognition. "
                            "Lista: "
                                """'Tequila José Cuervo Tradicional', 'Tequila José Cuervo Especial', 'Tequila Don Julio Blanco',
            'Tequila Don Julio Reposado', 'Tequila Don Julio 70', 'Tequila Herradura Plata', 'Tequila Herradura Reposado',
            'Tequila Herradura Añejo', 'Tequila Patrón Silver', 'Tequila Patrón Reposado', 'Tequila 1800 Blanco',
            'Tequila 1800 Reposado', 'Tequila Clase Azul Reposado', 'Tequila Clase Azul Añejo', 'Tequila Casa Dragones Blanco',
            'Tequila Casa Dragones Joven', 'Mezcal Montelobos Espadín', 'Mezcal Montelobos Tobalá', 'Mezcal Alipús San Andrés',
            'Mezcal Alipús San Baltazar', 'Mezcal Ojo de Tigre', 'Mezcal Los Amantes Reposado', 'Mezcal Los Amantes Joven',
            'Mezcal Del Maguey Vida', 'Mezcal Del Maguey Chichicapa', 'Mezcal Del Maguey Crema de Mezcal', 'Mezcal Bruxo No. 1',
            'Mezcal Bruxo No. 2', 'Mezcal Unión Joven', 'Mezcal Unión Viejo', 'Mezcal Amores Espadín', 'Mezcal Amores Cupreata',
            'Cerveza Corona Extra', 'Cerveza Corona Light', 'Cerveza Corona Familiar', 'Cerveza Modelo Especial',
            'Cerveza Negra Modelo', 'Cerveza Victoria', 'Cerveza Pacífico', 'Cerveza Pacífico Light', 'Cerveza Sol Clásica',
            'Cerveza Sol Michelada', 'Cerveza Indio', 'Cerveza Indio Pilsner Plata', 'Cerveza Dos Equis Lager',
            'Cerveza Dos Equis Ámbar', 'Cerveza Tecate Light', 'Cerveza Tecate Roja', 'Cerveza Heineken',
            'Cerveza Bud Light', 'Cerveza Michelob Ultra', 'Whisky Chivas Regal 12', 'Whisky Chivas Regal Extra',
            'Whisky Buchanan's 12', 'Whisky Buchanan's Master', 'Whisky Jack Daniel's Old No. 7', 'Whisky Jack Daniel's Honey',
            'Whisky Johnnie Walker Red Label', 'Whisky Johnnie Walker Black Label', 'Whisky Ballantine's Finest',
            'Vodka Absolut Azul', 'Vodka Absolut Citron', 'Vodka Smirnoff No. 21', 'Vodka Smirnoff Tamarindo',
            'Vodka Grey Goose', 'Vodka Stolichnaya', 'Vodka Belvedere', 'Ron Bacardí Blanco', 'Ron Bacardí Añejo',
            'Ron Bacardí Solera', 'Ron Havana Club 3 Años', 'Ron Havana Club Añejo 7 Años', 'Ron Captain Morgan',
            'Ron Malibu Coco', 'Brandy Presidente', 'Brandy Torres 10', 'Brandy Fundador', 'Brandy Azteca de Oro',
            'Vino Tinto Casillero del Diablo Cabernet Sauvignon', 'Vino Tinto Casillero del Diablo Merlot',
            'Vino Tinto Concha y Toro Reservado', 'Vino Blanco Santa Carolina', 'Vino Blanco Viña San Pedro',
            'Vino Espumoso Freixenet', 'Vino Rosado Barefoot', 'Vino Tinto Barefoot Merlot', 'Vino Blanco Casa Madero',
            'Vino Tinto Casa Madero Merlot', 'Vino Tinto L.A. Cetto Cabernet Sauvignon', 'Vino Tinto L.A. Cetto Petite Sirah',
            'Vino Blanco L.A. Cetto Chardonnay', 'Vino Blanco Monte Xanic', 'Vino Rosado Monte Xanic', 'Vino Espumoso Codorníu',
            'Licor de Café Kahlúa', 'Licor de Hierbas Jägermeister', 'Licor de Naranja Cointreau', 'Licor de Crema Bailey's Original',
            'Licor de Menta Peppermint', 'Anís Chinchón', 'Anís del Mono', 'Cognac Hennessy V.S', 'Cognac Rémy Martin V.S.O.P.',
            'Cognac Martell Cordon Bleu', 'Tequila Sauza Silver', 'Tequila Sauza Gold', 'Tequila Cazadores Blanco',
            'Tequila Cazadores Reposado', 'Mezcal Espina Negra Espadín', 'Mezcal Mezcaloteca Joven', 'Tequila Milagro Silver'
            , 'Shampoo Pantene Reparación', 'Shampoo Head & Shoulders Anticaspa', 'Shampoo Sedal Brillo',
            'Shampoo Dove Hidratación', 'Shampoo Herbal Essences Coco', 'Acondicionador Pantene Restauración',
            'Acondicionador Dove Nutrición', 'Acondicionador Head & Shoulders Suavidad', 'Jabón Zest Aqua',
            'Jabón Palmolive Naturals', 'Jabón Dove Original', 'Jabón Escudo Antibacterial', 'Jabón Protex Protección',
            'Jabón Líquido Palmolive Oliva', 'Gel Antibacterial Kleenex', 'Gel Antibacterial Escudo', 'Crema Nivea Soft',
            'Crema Corporal Lubriderm', 'Crema Corporal Jergens', 'Crema Corporal Neutrogena', 'Crema Corporal Dove',
            'Crema de Manos Nivea', 'Crema de Manos Atrix', 'Crema de Manos Palmolive', 'Pasta Dental Colgate Triple Acción',
            'Pasta Dental Crest 3D White', 'Pasta Dental Sensodyne', 'Pasta Dental Colgate Máxima Protección',
            'Enjuague Bucal Listerine Cool Mint', 'Enjuague Bucal Colgate Plax', 'Enjuague Bucal Crest', 
            'Desodorante Axe Dark Temptation', 'Desodorante Dove Invisible Dry', 'Desodorante Nivea Men Black & White',
            'Desodorante Rexona Clinical', 'Desodorante Lady Speed Stick', 'Desodorante Speed Stick Power',
            'Crema para Afeitar Gillette', 'Crema para Afeitar Nivea Men', 'Crema para Afeitar Barbasol',
            'After Shave Gillette', 'After Shave Nivea Men', 'Espuma para Afeitar Gillette Sensitive',
            'Rastrillos Gillette Mach3', 'Rastrillos Bic Flex3', 'Rastrillos Wilkinson Sword', 'Toallas Femeninas Kotex Nocturnas',
            'Toallas Femeninas Saba Buenas Noches', 'Toallas Femeninas Always Ultra', 'Tampones Tampax Regular',
            'Tampones Saba Compactos', 'Protector Diario Kotex', 'Protector Diario Always', 'Protector Diario Saba',
            'Papel Higiénico Pétalo Rendimax', 'Papel Higiénico Charmin Ultra', 'Papel Higiénico Regio', 
            'Papel Higiénico Suavel', 'Papel Higiénico Kleenex Cottonelle', 'Paños Húmedos Huggies', 
            'Paños Húmedos Kleenex', 'Paños Húmedos Cottonelle', 'Cotonetes Johnson\'s', 'Cotonetes Kleenex',
            'Cepillo de Dientes Colgate Extra Clean', 'Cepillo de Dientes Oral-B Cuidado Completo', 'Cepillo de Dientes Reach',
            'Cepillo de Dientes Colgate Sensitive', 'Crema Depilatoria Veet', 'Crema Depilatoria Nair', 'Cera Depilatoria Veet',
            'Acondicionador Pantene Fuerza y Brillo', 'Crema Ponds Clarant B3', 'Crema Nivea Reafirmante', 
            'Crema Corporal Jergens Hidratante', 'Crema Lubriderm Suavidad', 'Bloqueador Solar Nivea Factor 50',
            'Bloqueador Solar Hawaiian Tropic', 'Bloqueador Solar Banana Boat', 'Bloqueador Solar Neutrogena',
            'Shampoo para Bebé Johnson\'s Baby', 'Loción para Bebé Johnson\'s', 'Jabón para Bebé Huggies',
            'Aceite para Bebé Johnson\'s', 'Shampoo Head & Shoulders Mentol', 'Shampoo Caprice Herbal', 
            'Gel Fijador Ego Wet Look', 'Gel Fijador Moco de Gorila', 'Spray para el Cabello Pantene', 
            'Spray para el Cabello Tresemmé', 'Laca para el Cabello Elnett', 'Enjuague Bucal Biorepair',
            'Desodorante Secret Powder Fresh', 'Crema Antiarrugas L\'Oréal Revitalift', 'Crema Antiarrugas Olay Regenerist',
            'Gel Limpiador Facial Neutrogena', 'Gel Limpiador Facial La Roche-Posay Effaclar', 'Crema para Pies Neutrogena',
            'Crema para Pies Atrix', 'Crema Corporal Dove Hidratación Profunda', 'Protector Solar Bioderma Photoderm',
            'Protector Solar La Roche-Posay Anth', 'Cheetos Flaming Hot', 'Cheetos Bolita', 'Doritos Nacho', 'Doritos Flamin\' Hot', 'Doritos Pizzerola', 'Doritos Dinamita',
            'Sabritas Original', 'Sabritas Adobadas', 'Sabritas Limón', 'Ruffles Queso', 'Ruffles Mega Crunch', 'Ruffles Flamin\' Hot',
            'Takis Fuego', 'Takis Xplosion', 'Takis Nitro', 'Takis Zombie', 'Fritos Original', 'Fritos Chorizo y Chipotle',
            'Crujitos', 'Crujitos Flamin\' Hot', 'Churrumais', 'Churrumais Limón', 'Chicharrones Barcel', 'Chicharrones Del Rancho',
            'Chicharrones Pica Limón', 'Tostitos Original', 'Tostitos Salsa Verde', 'Tostitos Flamin\' Hot', 'Tostitos Guacamole',
            'Tostitos con Queso', 'Tostitos con Chile', 'Cacahuates Hot Nuts Original', 'Hot Nuts Flamin\' Hot',
            'Cacahuates De La Rosa', 'Cacahuates Japonés Nishikawa', 'Cacahuates con Chile Mafer', 'Papas Chips Churrumaiz',
            'Cacahuates Mafer Salados', 'Kranky Ricolino', 'Bubulubu Ricolino', 'Paleta Payaso Ricolino', 'Panditas Ricolino',
            'Rockaleta', 'Vero Mango', 'Vero Elote', 'Skwinkles Salsagheti', 'Skwinkles Rellenos', 'Pulparindo Tamarindo',
            'Pulparindo Mango', 'Rellerindos', 'Salsaguetis', 'Lucas Muecas', 'Lucas Gusano', 'Lucas Chamoy',
            'Pelón Pelo Rico', 'Pelón Pelo Rico Chamoy', 'Chamoy Miguelito', 'Miguelito Polvo', 'Chaca Chaca',
            'Gomitas de Ositos Haribo', 'Gomitas de Moritas Haribo', 'Gomitas de Fresas Haribo', 'Gomitas de Frutas Osito',
            'Gomitas de Frutas Miguelito', 'Panditas Enchilados', 'Picafresas', 'Picafresas Enchiladas', 'Choco Krispis Barritas',
            'Chocoretas', 'Panditas Trululu', 'Palomitas ACT II Mantequilla', 'Palomitas ACT II Queso', 'Palomitas ACT II Natural',
            'Palomitas PopCine', 'Palomitas Slim Pop', 'Tostitos Tiras', 'Tostitos Limón', 'Tostitos Queso Nacho',
            'Pringles Original', 'Pringles Queso', 'Pringles Cebolla', 'Pringles Jalapeño', 'Pringles Flamin\' Hot',
            'Cheetos Poffs', 'Doritos Diablo', 'Papitas Sabritas de Chile y Limón', 'Papitas Barcel Churritos',
            'Sabritas Adobadas Grandes', 'Sabritones Barcel', 'Churritos de Maíz Hot', 'Sabritones Limón',
            'Palomitas Barcel Banchos', 'Palomitas Barcel Bravitas', 'Palomitas Barcel Con Queso', 'Churrumais Asado',
            'Doritos Taco', 'Takis Intensos', 'Takis Nitro Limón', 'Takis Crunchy Fajita', 'Takis Churritos de Fuego',
            'Cacahuates Japoneses Hot Nuts', 'Cacahuates con Limón Hot Nuts', 'Cacahuates Enchilados Hot Nuts',
            'Bubulubu Minis', 'Skwinkles Chamoy', 'Salsagheti de Tamarindo', 'Paletas de Chile Rocaleta', 'Pulparindots'
            , 'La Costeña Chiles Chipotles', 'La Costeña Chiles Serranos', 'La Costeña Frijoles Bayos', 'Herdez Chipotles',
            'Herdez Jalapeños', 'McCormick Ajo en Polvo', 'McCormick Orégano', 'McCormick Pimienta Negra', 'Herdez Alcaparras',
            'Del Fuerte Puré de Tomate', 'Del Fuerte Salsa de Tomate', 'Knorr Suiza Caldo de Verduras', 'Knorr Suiza Caldo de Res',
            'Knorr Pasta Espagueti', 'Doña María Mole Poblano', 'Doña María Mole Verde', 'Sazonador Maggi', 'Rexal Polvo para Hornear',
            'Royal Polvo para Hornear', 'Tres Estrellas Masa para Tamal', 'Tres Estrellas Panque de Vainilla', 'San Marcos Jalapeños',
            'San Marcos Frijoles Refritos', 'Bachoco Muslo de Pollo', 'Bachoco Pechuga de Pollo', 'Pilgrim\'s Alas de Pollo',
            'Pilgrim\'s Pierna de Pollo', 'Capullo Aceite de Canola', 'Nutrioli Aceite de Maíz', 'Carbonell Aceite de Oliva',
            'La Fina Sal', 'Sabormex Sal', 'Ibarra Chocolate de Mesa', 'Abuelita Chocolate de Mesa', 'Alpura Crema Natural',
            'Alpura Leche Entera', 'Alpura Leche Deslactosada', 'Nestlé La Lechera Condensada', 'Nestlé Leche Evaporada',
            'Santa Clara Crema Natural', 'Bonafont Water Levite', 'Bonafont Agua Natural', 'Ciel Agua Natural',
            'Salsa Valentina Negra', 'Salsa Valentina Roja', 'La Morena Jalapeños', 'La Morena Chipotle', 'La Morena Salsa', 'Coca-Cola Regular', 'Coca-Cola Sin Azúcar', 'Pepsi Regular', 'Pepsi Black', 'Sabritas Clásicas',
            'Sabritas Adobadas', 'Sabritas Limón', 'Doritos Nacho', 'Doritos Flaming Hot', 'Cheetos Bolita',
            'Cheetos Torciditos', 'Ruffles Original', 'Ruffles Queso', 'Takis Fuego', 'Takis Nitro',
            'Barcel Chips', 'Barcel Mix', 'Barcel Churritos', 'Ricolino Bubulubu', 'Ricolino Paleta Payaso',
            'Ricolino Kranky', 'Ricolino Lunetas', 'Ricolino Duvalín', 'Marinela Gansito', 'Marinela Pingüinos',
            'Marinela Choco Roles', 'Marinela Submarinos', 'Marinela Pinguinos de Fresa', 'Bimbo Pan Blanco',
            'Bimbo Pan Integral', 'Bimbo Conchas', 'Bimbo Mantecadas', 'Bimbo Roles de Canela', 'Wonder Pan Integral',
            'Wonder Pan Blanco', 'Ruffles Mega Crunch', 'Gamesa Emperador Chocolate', 'Gamesa Emperador Limón',
            'Gamesa Chokis', 'Gamesa Marias', 'Gamesa Saladitas', 'Oreo Clásicas', 'Oreo Golden', 'Oreo Mini',
            'Nescafé Clásico', 'Nescafé Decaf', 'Nescafé Dolca', 'Nescafé Gold', 'La Costeña Chiles Jalapeños',
            'La Costeña Frijoles Refritos', 'La Costeña Salsas', 'La Costeña Chiles en Escabeche', 'Herdez Salsa Casera',
            'Herdez Salsa Verde', 'Herdez Guacamole', 'McCormick Mayonesa', 'McCormick Mostaza', 'McCormick Catsup',
            'Barcel Takis Xplosion', 'Pepsi Manzana', 'Ciel Agua Natural', 'Bonafont Agua Natural', 'Jumex Néctar de Mango',
            'Jumex Néctar de Durazno', 'Jumex Néctar de Manzana', 'Del Valle Jugo de Naranja', 'Del Valle Néctar de Manzana',
            'Del Valle Frutopia', 'Nutrileche Leche Entera', 'Nutrileche Leche Deslactosada', 'Santa Clara Leche Deslactosada',
            'Lala Yogur Natural', 'Lala Yogur de Fresa', 'Danone Activia Natural', 'Danone Danonino', 'Danone Yoplait Griego',
            'Danone Vitalínea', 'Nestlé Nido', 'Nestlé Svelty', 'Nestlé La Lechera', 'Nestlé Carnation Clavel',
            'Abuelita Chocolate en Polvo', 'Hershey\'s Chocolate en Polvo', 'Choco Milk Polvo', 'Gerber Papilla de Manzana',
            'Gerber Papilla de Plátano', 'Suero Oral Pedialyte', 'Electrolit Naranja', 'Gatorade Azul', 'Gatorade Uva',
            'Powerade Azul', 'Powerade Naranja', 'Halls Mentol', 'Halls Sandía', 'Trident Menta', 'Trident Fresa',
            'Lala Queso Panela', 'Lala Queso Oaxaca', 'Philadelphia Queso Crema', 'Santa Clara Crema Natural',
            'Nutella', 'Skippy Crema de Cacahuate', 'Maruchan Ramen de Pollo', 'Maruchan Ramen de Camarón',
            'Knorr Suiza Caldo de Pollo', 'La Moderna Pasta de Coditos', 'La Moderna Pasta de Espagueti', 'Maseca Harina de Maíz',
            'Tres Estrellas Harina de Trigo', 'Minsa Harina de Maíz', 'Gamesa Galletas Marias', 'Gamesa Canelitas',
            'Gamesa Mamut', 'Quaker Avena', 'Karo Miel de Maíz', 'Ajumex Pulparindo', 'Ajumex Rellerindos', 'Pulparindo Mini',
            'Mazapán De La Rosa', 'Marinela Sponch', 'Marinela Chocotorro', 'Marinela Gansito', 'Coca-Cola Light',
            'Sprite Sin Azúcar', 'Fanta Naranja', 'Fanta Fresa', 'Dr. Pepper', 'Canada Dry Ginger Ale',
            'Topo Chico Agua Mineral', 'Agua Electrolit Coco',
            'Agua Electrolit Fresa', 'Yoli Refresco de Limón', 'Manzanita Sol', 'Lala Lala Milkshake', 'Santa Clara Crema',
            'Santa Clara Yogur Natural', 'Santa Clara Yogur Fresa', 'Zucaritas de Kellogg\'s', 'Corn Flakes de Kellogg\'s',
            'All Bran de Kellogg\'s', 'Honey Nut Cheerios', 'Trix de General Mills', 'Choco Krispis de Kellogg\'s',
            'Nestlé Crunch', 'KitKat', 'Carlos V', 'Carlos V Blanco', 'Toblerone', 'Ferrero Rocher', 'M&M\'s',
            'M&M\'s Peanut', 'Snickers', 'Milky Way', 'Twix', 'Bubulubu', 'Pulparindo', 'Skwinkles', 'Salsaguetis',
            'Rockaleta', 'Canel\'s Chicle', 'Trident Sin Azúcar', 'Orbit', 'Coca-Cola Zero', 'Fresca Cítrica',
            'Sidral Mundet', 'Ciel Mineralizada', 'Bonafont Kids', 'Bonafont Levite Limón', 'Jumex Antiox',
            'Del Valle Néctar Durazno', 'Cheetos Poffs', 'Fritos Sabritas', 'Crujitos', 'Picafresas',
            'Chocoretas', 'Oreo Red Velvet', 'Gamesa Animalitos', 'Gamesa Bombones', 'Gamesa Saladitas',
            'Marinela Twinkie', 'Herdez Guacamole Salsa', 'Herdez Salsa Verde Casera', 'Herdez Salsa Roja Casera',
            'Bimbo Mantecadas', 'Bimbo Negrito', 'Bimbo Cuernitos', 'Bimbo Roles', 'Bimbo Chocolatín',
            'Gamesa Florentinas', 'Gamesa Empanadas de Piña', 'Nutrileche Leche Light', 'Nestlé Nescafé Decaf',
            'Nestlé Nescafé Cappuccino', 'Lala Yogur Frutos Rojos', 'Philadelphia Dip', 'Danone Activia Ciruela',
            'Danone Yoplait Griego Natural', 'Danone Yoplait Griego Mango', 'Santa Clara Nieve Vainilla',
            'Santa Clara Nieve Chocolate', 'Santa Clara Paleta Chocolate', 'Bubulubu Minis', 'Duvalín Choco-Vainilla'
            """
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            f"A partir de la siguiente instrucción: {instruction}. "
                            "En caso de que se te indique algo relacionado con la venta de un producto, regresa la cantidad en número y el producto "
                            "en string en este formato: cantidad|producto. No uses apóstrofes ni ningún carácter extra. "
                            "Si no encuentras ningún producto, regresa 0|'el producto que tu desees aleatorio de los proporcionados' y no añadas nada más."
                        )
                    }
                ]
        
            )
            answer = completion.choices[0].message.content.strip()
            print(answer)
            cantidad = answer.split("|")[0]
            producto = answer.split("|")[1] 

            # Utiliza thefuzz para encontrar la coincidencia más cercana del producto en la lista
            producto_match = process.extractOne(producto, self.productos)
            return producto_match[0], cantidad
        
    def parse_instruction2(self, instruction):
        # Llama al modelo de OpenAI para interpretar la instrucción
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an inventory management assistant."},
                {
                    "role": "user",
                    "content": f"A partir de la siguiente instrucción: {instruction}. se te va a dar un numero "
                               f"identificalo y regresalo solito, sin ningun caracter extra, solo quiero que me regreses el numero, no me digas nada mas PORFAVOR."
                }
            ]
        )
        
        answer = completion.choices[0].message.content.strip() 
        numero = process.extractOne(answer, self.numeros)

        return int(numero[0])
    
