import matplotlib.pyplot as plt

import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab


import matplotlib.transforms as mtransforms

from mpl_toolkits.agg_filter import FilteredArtistList, GrowFilter, \
     DropShadowFilter, LightFilter

def filtered_text(ax):
    # mostly copied from contour_demo.py

    # prepare image
    delta = 0.025
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    # difference of Gaussians
    Z = 10.0 * (Z2 - Z1)


    # draw
    im = ax.imshow(Z, interpolation='bilinear', origin='lower',
                   cmap=cm.gray, extent=(-3,3,-2,2))
    levels = np.arange(-1.2, 1.6, 0.2)
    CS = ax.contour(Z, levels,
                    origin='lower',
                    linewidths=2,
                    extent=(-3,3,-2,2))

    ax.set_aspect("auto")

    # contour label
    cl = ax.clabel(CS, levels[1::2],  # label every second level
                   inline=1,
                   fmt='%1.1f',
                   fontsize=11)

    # change clable color to black
    from matplotlib.patheffects import Normal
    for t in cl:
        t.set_color("k")
        t.set_path_effects([Normal()]) # to force TextPath (i.e., same font in all backends)

    # Add white glows to improve visibility of labels.
    white_glows = FilteredArtistList(cl, GrowFilter(3))
    ax.add_artist(white_glows)
    white_glows.set_zorder(cl[0].get_zorder()-0.1)

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)


def drop_shadow_line(ax):
    # copyed from examples/misc/svg_filter_line.py

    # draw lines
    l1, = ax.plot([0.1, 0.5, 0.9], [0.1, 0.9, 0.5], "bo-",
                  mec="b", mfc="w", lw=5, mew=3, ms=10, label="Line 1")
    l2, = ax.plot([0.1, 0.5, 0.9], [0.5, 0.2, 0.7], "ro-",
                  mec="r", mfc="w", lw=5, mew=3, ms=10, label="Line 1")


    gauss = DropShadowFilter(4, offsets=(4, -6))

    shadow = FilteredArtistList([l1, l2], gauss)
    ax.add_artist(shadow)
    shadow.set_zorder(l1.get_zorder()-0.1)

    ax.set_xlim(0., 1.)
    ax.set_ylim(0., 1.)

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)




def drop_shadow_patches(ax):
    # copyed from barchart_demo.py
    N = 5
    menMeans = (20, 35, 30, 35, 27)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    rects1 = ax.bar(ind, menMeans, width, color='r', ec="w", lw=2)

    womenMeans = (25, 32, 34, 20, 25)
    rects2 = ax.bar(ind+width+0.1, womenMeans, width, color='y', ec="w", lw=2)

    gauss = DropShadowFilter(5, offsets=(1,1), )
    shadow = FilteredArtistList(rects1+rects2, gauss)
    ax.add_artist(shadow)
    shadow.set_zorder(rects1[0].get_zorder()-0.1)

    ax.set_xlim(ind[0]-0.5, ind[-1]+1.5)
    ax.set_ylim(0, 40)

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)


def light_filter_pie(ax):
    fracs = [15,30,45, 10]
    explode=(0, 0.05, 0, 0)
    pies = ax.pie(fracs, explode=explode)
    ax.patch.set_visible(True)

    light_filter = LightFilter(9)
    for p in pies[0]:
        p.set_agg_filter(light_filter)
        p.set_rasterized(True) # to support mixed-mode renderers
        p.set(ec="none",
              lw=2)

    gauss = DropShadowFilter(9, offsets=(3,4), alpha=0.7)
    shadow = FilteredArtistList(pies[0], gauss)
    ax.add_artist(shadow)
    shadow.set_zorder(pies[0][0].get_zorder()-0.1)


if 1:
 
    plt.figure(1, figsize=(6, 6))
    plt.subplots_adjust(left=0.05, right=0.95)

    ax = plt.subplot(221)
    filtered_text(ax)

    ax = plt.subplot(222)
    drop_shadow_line(ax)

    ax = plt.subplot(223)
    drop_shadow_patches(ax)

    ax = plt.subplot(224)
    ax.set_aspect(1)
    light_filter_pie(ax)
    ax.set_frame_on(True)

    plt.show()


