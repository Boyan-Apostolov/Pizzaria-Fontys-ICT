# Mario & Luigi's Pizzaria

<p align="center">
  <img src="https://i.ibb.co/T4t5FNZ/SCR-20231112-kppi.png">
</p>

Flask web application to manage pizza orders in a local applications. This project is made in a group for Semester 1 @ Fontys ICT, Eindhoven

Originally the application was commited to the following repo in GitLAB with the other group members: https://gitlab.com/boian4934/pizzaria-fontys-ict but I am forking it to my personal GitHub

# 🛠 Built with:

- Python
- Flask
- Arduino


# # 👥 Group members:

- [Boyan Apostolov](https://github.com/Boyan-Apostolov) -> Backend & Flask
- [Victor Stoica](https://gitlab.com/victorcristianstoica17) -> Arduino
- [Fatih Durmaz](https://gitlab.com/sameddurmaz) -> Communication & Schedules
- [Djairo Nous](https://gitlab.com/Dwn-dev) -> Design & Ideas

# Permissions:

| **Permissions**          | Guest/Customer | Mario | Luigi |
| ------------------------ | -------------- | ----- | ----- |
| Lading/Home page| ✅| ✅| ✅|
| Contact & Info| ✅| ✅| ✅|
| Menu| ✅| ✅| ✅|
| Ready orders screen|✅|✅|✅
| Login| ❌|  ✅| ✅|
| Current orders| ❌| ✅|✅|
| Cashier dashboard| ❌|✅|  ❌|
| Placing an order | ✅| ✅| ❌|
| Accepting orders| ❌| ✅|❌ |
| Declining orders| ❌| ✅|❌| 
| Cook dashboard| ❌| ❌| ✅|
| Cooking orders| ❌| ❌| ✅|

# Pages:

**Home page**

This is the landing page of the application, here the user chooses to make an order or view the info page
![Home Page](https://i.ibb.co/wYWx5zF/SCR-20231112-kfpi.png)

**Info & Contact page**

This page shows general information for the pizzaria.
![Contact page](https://i.ibb.co/fSphbw4/SCR-20231112-khmd.png)

**Menu page**

This is the main page that customers use. From here clients can filter the available pizzas as well as order a chosen pizza. The selection of quantity is done using a sweetalert2 popup.
![Menu Page](https://i.ibb.co/vVnWCk2/SCR-20231112-kifz.png)

![Quantity select](https://i.ibb.co/QFXBfkH/SCR-20231112-kiww.png)

**Order complete page**

This pages give the customer their order number as well as an aproximate time for pickup of the pizza.
![Order complete Page](https://i.ibb.co/0fjdnK8/SCR-20231112-kjcq.png)

**Login page**

The login page is accessible only to Mario and Luigi using the preset passwords in order to manage the pizzaria. Customers do not need an account to order
![Login Page](https://i.ibb.co/xg4cDrj/SCR-20231112-kkxv.png)


**Cashier dashboard page**

On this page the cashier finds useful information of the pizzaria - total orders, revenue, most ordered pizzas and a chart for the orders per hour. Every 5 seconds a background check for new orders is initiated and a popup is shown (second photo)
![Cashier dashboard](https://i.ibb.co/SQVfG15/SCR-20231112-kkji.png)
![Popup](https://i.ibb.co/2cJWWjX/SCR-20231112-kjqj.png)

**New order page**

On this page, Mario can either accept or decline an order. If an order is accepted, it is sent to Luigi for preparation and if it is declined, Mario can write in a reason for declining.
![New order Page](https://i.ibb.co/p2h4F7V/SCR-20231112-klzv.png)
![Accepted order](https://i.ibb.co/mSHrR0J/SCR-20231112-kmmt.png)
![Declined order](https://i.ibb.co/NScs8gX/SCR-20231112-kmvt.png)

**Current orders page**

This page shows the current status of the orders. Mario and Luigi can control the orders from here
![Home Page](https://i.ibb.co/0tN0BhW/SCR-20231112-knov.png)

**Luigi Smart oven page**

When an order is sent to the Smart oven (Arduino) the status is automatically changed and the details for the order as well as the temperature and remaining time in the oven are shown on the screen
![Oven Page](https://i.ibb.co/nLKbSc9/SCR-20231112-knnc.png)

**Orders screen**

This page is shown on monitors in the pizzaria for the customers so that they know when their order is done and ready to be picked up from the counter. When an order is given to the customer, Mario marks it as delivered and it disappears from the screen.
![Screen Page](https://i.ibb.co/7NPsGFG/SCR-20231112-kouq.png)

