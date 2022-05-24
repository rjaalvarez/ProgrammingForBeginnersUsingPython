class Customers:
    greeting = "Welcome to the Coffee Palace!"

customer_1 = Customers()
customer_1.name = "Samirah"
customer_1.beverage = "Iced caffe latte"
customer_1.food = "Cinnamon roll"
customer_1.total = 225

customer_2 = Customers()
customer_2.name = "Jerry"
customer_2.beverage = "Caramel macchiato"
customer_2.food = "Glazed doughnut"
customer_2.total = 230

print(Customers.greeting)
print(customer_1.beverage)
print(customer_2.food)
