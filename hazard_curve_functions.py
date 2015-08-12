from pylab import *

def hazard_curve(event_list, hmax=None):
    if hmax is None:
        hmax = array([E[1] for E in event_list]).max() * 1.1
    h_ev = linspace(0,hmax,500)
    p_ev = 1e-9 * ones(h_ev.shape)
    for E in event_list:
        p_E = E[0]
        h_E = E[1]
        p_ev = where(h_E <= h_ev, p_ev, 1. - (1-p_ev)*(1-p_E))
    return h_ev, p_ev
        

def p_interp(h,h_ev,p_ev):
    if h > h_ev.max():
        return 1e-9
    k = find(h_ev > h).min()
    alpha = (h - h_ev[k-1]) / (h_ev[k] - h_ev[k-1])
    # print k, h_ev[k-1], h_ev[k], alpha
    p = alpha * p_ev[k] + (1.-alpha)*p_ev[k-1]
    if p < 1e-8:
        p = 0.
    return p

def plot_hazard_curve(h_ev,p_ev):
    fig = figure(figsize=(15,4))
    subplot(121)
    semilogy(h_ev,p_ev)
    ylim(1e-4, 1)
    xlabel("h (exceedance value) in meters")
    ylabel("probability")
    title("Annual probability that flooding depth exceeds h")
    text(h_ev[-1]*0.6, 4e-1, 'For example:')
    h = 0.3
    p = p_interp(h,h_ev,p_ev)
    text(h_ev[-1]*0.6, 2e-1, 'P(%4.2f) = %8.6f' % (h,p))
    h = 1.3
    p = p_interp(h,h_ev,p_ev)
    text(h_ev[-1]*0.6, 1e-1, 'P(%4.2f) = %8.6f' % (h,p))
    h = 1.8
    p = p_interp(h,h_ev,p_ev)
    text(h_ev[-1]*0.6, 5e-2, 'P(%4.2f) = %8.6f' % (h,p))
    subplot(122)
    plot(h_ev,p_ev)
    ylim(-0.0001,p_ev[0]*1.5)
    title("On linear p scale")
    return fig
    
def makefig(h2,p2):
    p1 = 0.001
    h1 = 1.5
    E1 = [p1,h1]
    E2 = [p2,h2]
    event_list = [E1, E2]
    h_ev,p_ev = hazard_curve(event_list, 3)
    fig = plot_hazard_curve(h_ev,p_ev)
    ax = fig.axes[0]
    ax.text(0.5, 1e-1, 'h2 = %3.1f' % h2)
    return fig
    
