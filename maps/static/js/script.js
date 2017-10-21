ymaps.ready(function () {
    var projection = new ymaps.projection.Cartesian([
        [0, 0],
        [1, 1]
    ]);

    var map = new ymaps.Map('map', {
        center: [0, 0],
        zoom: 1,
        type: new ymaps.MapType('Карта офиса', [OfficeLayer]),
        projection: projection
    });

    function OfficeLayer() {
        var layer = new ymaps.Layer('/map/tiles/%z/%y/%x.png', {
            projection: projection
        });

        layer.getZoomRange = function () {
            return ymaps.vow.resolve([1, 5]);
        };

        return layer;
    }
});
