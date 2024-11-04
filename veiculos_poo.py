import sqlite3

class Veiculo:
    def conexao(self):
        conexao = sqlite3.connect("estacaoCarregamento_db.db")
        consulta = conexao.cursor()
        tabela = """
        CREATE TABLE IF NOT EXISTS veiculos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            placa VARCHAR(100),
            modelo TEXT,
            status TEXT,
            tempo_carregamento FLOAT
        );
        """
        consulta.execute(tabela)
        return conexao

    def cadastrarVeiculo(self, placa, modelo, tempo_carregamento=10):
        conexao = self.conexao()
        sql = "INSERT INTO veiculos VALUES (NULL, ?, ?, ?, ?)"
        campos = (placa, modelo, "Disponível", tempo_carregamento)
        consulta = conexao.cursor()
        consulta.execute(sql, campos)
        conexao.commit()
        print("Veículo cadastrado com sucesso!")
        conexao.close()

    def consultarVeiculos(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "SELECT * FROM veiculos"
        consulta.execute(sql)
        veiculos = consulta.fetchall()
        for veiculo in veiculos:
            print(f"ID: {veiculo[0]}, Placa: {veiculo[1]}, Modelo: {veiculo[2]}, Status: {veiculo[3]}, Tempo de Carregamento: {veiculo[4]}")
        conexao.close()

    def iniciarCarregamento(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "UPDATE veiculos SET status = 'Em Carregamento' WHERE id = ? AND status = 'Disponível'"
        consulta.execute(sql, (id,))
        conexao.commit()
        if consulta.rowcount > 0:
            print("Carregamento iniciado.")
        else:
            print("Não foi possível iniciar o carregamento. Verifique o status do veículo.")
        conexao.close()

    def finalizarCarregamento(self, id, custo_por_hora):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql_select = "SELECT tempo_carregamento FROM veiculos WHERE id = ? AND status = 'Em Carregamento'"
        consulta.execute(sql_select, (id,))
        resultado = consulta.fetchone()
        if resultado:
            tempo_carregamento = resultado[0]
            custo_total = tempo_carregamento * custo_por_hora
            sql_update = "UPDATE veiculos SET status = 'Carregamento Finalizado' WHERE id = ?"
            consulta.execute(sql_update, id,)
            conexao.commit()
            print(f"Carregamento finalizado. Custo total: R$ {custo_total:.2f}")
        else:
            print("O veículo não está em carregamento.")
        conexao.close()

    def consultarStatus(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "SELECT * FROM veiculos WHERE id = ?"
        consulta.execute(sql, (id,))
        veiculo = consulta.fetchone()
        if veiculo:
            print(f"ID: {veiculo[0]}, Placa: {veiculo[1]}, Modelo: {veiculo[2]}, Status: {veiculo[3]}, Tempo de Carregamento: {veiculo[4]}")
        else:
            print("Veículo não encontrado.")
        conexao.close()

    def deletarVeiculo(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "DELETE FROM veiculos WHERE id = ?"
        consulta.execute(sql, (id,))
        conexao.commit()
        if consulta.rowcount > 0:
            print("Veículo deletado com sucesso.")
        else:
            print("Veículo não encontrado.")
        conexao.close()
