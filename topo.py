from mininet.topo import Topo

class DelayTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')

        # Hosts on switch 1 — low delay
        self.addLink(h1, s1, delay='5ms')
        self.addLink(h2, s1, delay='5ms')

        # Hosts on switch 2 — higher delay
        self.addLink(h3, s2, delay='20ms')
        self.addLink(h4, s2, delay='20ms')

        # Inter-switch link
        self.addLink(s1, s2, delay='10ms')

topos = {'delaytopo': DelayTopo}
