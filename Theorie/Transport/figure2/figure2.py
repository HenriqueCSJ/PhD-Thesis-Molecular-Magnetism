execfile("Transport/CB_classique.py")
fig = figure()
plot(x,fer(x,0,1,0.001))
plot(x,fer(x,0,1,0.01))
plot(x,fer(x,0,1,0.05))
plot(x,fer(x,0,1,0.1))
xlabel(r"$\mu-\mu_{\rm{F}}$")
ylabel(r"$p(\mu-\mu_{\rm{F}})$")
ax = gca()
l1 = ax.lines[0]
l2 = ax.lines[1]
l3 = ax.lines[2]
l4 = ax.lines[3]
l1.set_label(r"$T = 0.001\mu_{\rm{F}}$")
l2.set_label(r"$T = 0.01\mu_{\rm{F}}$")
l3.set_label(r"$T = 0.05\mu_{\rm{F}}$")
l4.set_label(r"$T = 0.1\mu_{\rm{F}}$")
legend()
fig.savefig("Theorie/Transport/figure2/figure2.pdf")
