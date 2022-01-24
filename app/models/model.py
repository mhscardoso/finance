import sqlite3

class Banco:

    def __init__(self):
        self.connection = sqlite3.connect("../../base.db")
        self.createTables()
    
    def createTables(self):

        cursor = self.connection.cursor()

        # Criando usuario
        cursor.execute("""
        create table if not exists users (
            id integer primery key,
            username text not null,
            hash_pass text not null,
            cash decimal default 10000.00
        )
        """)

        # Criando tabela compra
        cursor.execute(
        """
        create table if not exists buy (
            user integer foreing key references users(id),
            stock text not null,
            price decimal,
            shares integer
        )
        """
        )

        # Criando tabela venda
        cursor.execute(
        """
        create table if not exists sell (
            user integer foreing key references users(id),
            stock text not null,
            price decimal,
            shares integer            
        )
        """
        )

        # Criando tabela historico
        cursor.execute(
        """
        create table if not exists history (
            user integer foreing key references users(id),
            stock text not null,
            price decimal,
            shares integer,
            operation integer            
        )
        """
        )

        self.connection.commit()
        cursor.close()
    

    # Inserindo usuarios da tabela
    def insereUsuario(self, username, password):
        
        if len(self.procuraUsername(username)) != 0:
            return "Usuario ja existente"
        
        cursor = self.connection.cursor()
        cursor.execute(
            """
            insert into users (username, hash_pass) VALUES (?, ?)
            """, (username, password,)
        )

        self.connection.commit()
        cursor.close()

        return "Usuario cadastrado com sucesso"
    
    # Confere os dados para o login
    def confereDados(self, username, password):

        user = self.procuraUsername(username)
        if len(user) != 1:
            return False

        if user[0][2] != password:
            return False
        return True


    # Retorna os dados de um usuario especifico
    def procuraUsername(self, username):
        cursor = self.connection.cursor()

        cursor.execute("select * from users where username = ?", (username,))
        self.connection.commit()
        rows = cursor.fetchall()
        cursor.close()
        
        return rows
    

    def buy_model(self, user_id, stock, price, shares, new_cash):
        cursor = self.connection.cursor()

        cursor.execute("insert into buy (user, stock, price, shares) values (?, ?, ?, ?)", (user_id, stock.upper(), price, shares,))
        cursor.execute("insert into history (user, stock, price, shares, operation) values (?, ?, ?, ?, ?)", (user_id, stock.upper(), price, shares, 0,))
        cursor.execute("update users set cash = ? where id = ?", (new_cash, user_id,))

        self.connection.commit()
        cursor.close()
    

    def retornaQuoteComprada(self, user_id, quote):
        cursor = self.connection.cursor()

        cursor.execute("select * from buy where user = ? and stock = ?", (user_id, quote,))
        self.connection.commit()
        rows_bought = cursor.fetchall()
        cursor.close()
        
        return rows_bought

    def retornaQuoteVedida(self, user_id, quote):
        cursor = self.connection.cursor()

        cursor.execute("select * from sell where user = ? and stock = ?", (user_id, quote,))
        self.connection.commit()
        rows_sold = cursor.fetchall()
        cursor.close()
        
        return rows_sold
    
    
    def stocks(self, user_id, quote):
        comprados = self.retornaQuoteComprada(user_id, quote)

        if len(comprados) == 0:
            return 0

        vendidos = self.retornaQuoteVedida(user_id, quote)

        shares_compradas = 0
        shares_vendidas = 0

        for operation in comprados:
            shares_compradas += operation[3]
        
        if len(vendidos) == 0:
            return shares_compradas
        
        for operation in vendidos:
            shares_vendidas += operation[3]

        remain_shares = shares_compradas - shares_vendidas
        return remain_shares
    

    def sell_model(self, user_id, stock, price, shares, new_cash):
        cursor = self.connection.cursor()

        cursor.execute("insert into sell (user, stock, price, shares) values (?, ?, ?, ?)", (user_id, stock.upper(), price, shares,))
        cursor.execute("insert into history (user, stock, price, shares, operation) values (?, ?, ?, ?, ?)", (user_id, stock.upper(), price, shares, 1,))
        cursor.execute("update users set cash = ? where id = ?", (new_cash, user_id,))

        self.connection.commit()
        cursor.close()
        
    

        
