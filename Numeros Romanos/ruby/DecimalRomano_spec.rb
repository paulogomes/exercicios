# require 'DecimalRomano.rb'
# 
# describe Integer do
# 
#   it "deveria retornar o numero em romano" do
# 
#     File.readlines('../teste.txt').each do | linha |
#       decimal,romano = linha.split('=')
#       decimal.to_i.em_romano.should == romano.to_s
#     end
# 
#   end
# 
# end
# 

File.readlines('../teste.txt').each do | linha |
  puts linha.split(\n)
end