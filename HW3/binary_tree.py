from mininet.topo import Topo
class BinaryTreeTopo( Topo ):
    "Binary Tree Topology Class."
    def __init__( self ):
        "Create the binary tree topology."
        # Initialize topology
        Topo.__init__( self )
     # Add hosts
        leafHost1 = self.addHost( 'h1' )
        leafHost2 = self.addHost( 'h2' )
        leafHost3 = self.addHost( 'h3' )
        leafHost4 = self.addHost( 'h4' )    
        leafHost5 = self.addHost( 'h5' )
        leafHost6 = self.addHost( 'h6' )
        leafHost7 = self.addHost( 'h7' )
        leafHost8 = self.addHost( 'h8' )
     # Add switches
        rootSwitch = self.addSwitch( 's1' )
        midSwitch1 = self.addSwitch( 's2' )
        midSwitch2 = self.addSwitch( 's3' )
        midSwitch3 = self.addSwitch( 's4' )
        midSwitch4 = self.addSwitch( 's5' )
        midSwitch5 = self.addSwitch( 's6' )
        midSwitch6 = self.addSwitch( 's7' )
     # Add links
        self.addLink( leafHost1, midSwitch2 )
        self.addLink( leafHost2, midSwitch2 )
        self.addLink( leafHost3, midSwitch3 )
        self.addLink( leafHost4, midSwitch3 )
        self.addLink( leafHost5, midSwitch5 )
        self.addLink( leafHost6, midSwitch5 )
        self.addLink( leafHost7, midSwitch6 )
        self.addLink( leafHost8, midSwitch6 )
        self.addLink( midSwitch2, midSwitch1 )
        self.addLink( midSwitch3, midSwitch1 )
        self.addLink( midSwitch5, midSwitch4 )
        self.addLink( midSwitch6, midSwitch4 )
        self.addLink( midSwitch1, rootSwitch )
        self.addLink( midSwitch4, rootSwitch )
topos = { 'binary_tree': ( lambda: BinaryTreeTopo() ) }
