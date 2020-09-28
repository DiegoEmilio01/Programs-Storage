class ReyOgro
    attr_reader :nombre
    def initialize
        @nombre = "I am Melkor, king of the Orcs"
    end
end
class ReyElfo
    attr_reader :nombre
    def initialize
        @nombre = "I am Thranduil, king of the Elfs"
    end
end
class ReyHumano
    attr_reader :nombre
    def initialize
        @nombre = "I am Aragorn, king of the Humans"
    end
end

class FactReyOgro
    def create
        ReyOgro.new
    end
end
class FactReyElfo
    def create
        ReyElfo.new
    end
end
class FactReyHumano
    def create
        ReyHumano.new
    end
end

class CastilloOgro
    attr_reader :nombre
    def initialize
        @nombre = "This is Isengard, home of the Orcs"
    end
end
class CastilloElfo
    attr_reader :nombre
    def initialize
        @nombre = "This is Woodlands, home of the Elfs"
    end
end
class CastilloHumano
    attr_reader :nombre
    def initialize
        @nombre = "This is Silmarillion, home of the Humans"
    end
end

class FactCastilloOgro
    def create
        CastilloOgro.new
    end
end
class FactCastilloElfo
    def create
        CastilloElfo.new
    end
end
class FactCastilloHumano
    def create
        CastilloHumano.new
    end
end

class EjercitoOgro
    attr_reader :descripcion
    def initialize
        @descripcion = "This is the powerful Goblins army composed of 20000 Orcs"
        @efectivos = 20000
    end
end
class EjercitoElfo
    attr_reader :descripcion
    def initialize
        @descripcion = "This is the powerful Elves army composed of 2500 Elfs"
        @efectivos = 2500
    end
end
class EjercitoHumano
    attr_reader :descripcion
    def initialize
        @descripcion = "This is the powerful Soldiers army composed of 4500 Humans"
        @efectivos = 4500
    end
end

class FactEjercitoOgro
    def create
        EjercitoOgro.new
    end
end
class FactEjercitoElfo
    def create
        EjercitoElfo.new
    end
end
class FactEjercitoHumano
    def create
        EjercitoHumano.new
    end
end

class Realm
    attr_reader :rey, :castillo, :ejercito
    def initialize (rey, castillo, ejercito)
        @rey = rey.create
        @castillo = castillo.create
        @ejercito = ejercito.create
    end
    def describe
        puts @rey.nombre
        puts @castillo.nombre
        puts @ejercito.descripcion
    end
end

fact_rey_ogro = FactReyOgro.new
fact_castillo_ogro = FactCastilloOgro.new
fact_ejercito_ogro = FactEjercitoOgro.new

reino = Realm.new(fact_rey_ogro, fact_castillo_ogro, fact_ejercito_ogro)
reino.describe
puts reino.rey.nombre