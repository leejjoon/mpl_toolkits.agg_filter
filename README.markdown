This module provides classes that can be used to set agg_filter's for
matplotlib.

![sample](https://raw.github.com/leejjoon/mpl_toolkits.agg_filter/master/doc/_static/example.png)

For example, ::

    from mpl_toolkits.agg_filter import LightFilter

    light_filter = LightFilter(9)
    p.set_agg_filter(light_filter) # p is some artist

Often used filter is the drop shadow filter. ::

    l1, = plt.plot([0.1, 0.5, 0.9], [0.1, 0.9, 0.5], "bo-",
                   mec="b", mfc="w", lw=5, mew=3, ms=10, label="Line 1")

    from mpl_toolkits.agg_filter import DropShadowFilter
    gauss = DropShadowFilter(4, offsets=(4, -6))

    shadow = FilteredArtistList([l1], gauss)
    ax.add_artist(shadow)
    shadow.set_zorder(l1.get_zorder()-0.1)


