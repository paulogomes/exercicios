class Fixnum

  def em_romano

    # Converte número Decimal para Romano

    unidade = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    dezena  = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    centena = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    milhar  = ['', 'M', 'MM', 'MMM']

    lista = [unidade, dezena, centena, milhar]

    numero = self.to_s.reverse
    casa_decimal = numero.length
    resultado = ''

    casa_decimal.times do
      casa_decimal = casa_decimal - 1
      resultado = resultado + lista[casa_decimal][numero[casa_decimal].to_i]
    end

    resultado

  end

end