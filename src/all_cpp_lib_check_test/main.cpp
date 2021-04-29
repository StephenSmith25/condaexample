#include "tbb/concurrent_unordered_map.h" // tbb
#include "boost/hana/basic_tuple.hpp" // boost
#include "Poco/File.h"
#include "nexus/napi.h"
#include "H5Cpp.h"
#include "gsl/gsl_sf_bessel.h"
#include "json/json.h"
#include "librdkafka/rdkafkacpp.h"
#include <QString>
#include <QBitmap>
#include <QCheckBox>
#include <QOpenGLBuffer>
#include <QTestEventList>
#include <QHelpSearchResult>
#include <QtConcurrent>
#include <QDomAttr>
#include <QWebFrame>
#include <QDnsLookup>
#include <QPrinter>
#include "Qsci/qscistyle.h"
#include <cxxtest/TestSuite.h>

int main() {
    // tbb check
    tbb::concurrent_unordered_multimap<std::string, int> iterator;
    // Boost check
    constexpr auto zs = boost::hana::make_basic_tuple(1, '2', 3.3);
    // Poco check
    const auto file = Poco::File();
    // NeXus check
    NXMDisableErrorReporting();
    // hdf5
    const H5std_string h5string = "test";
    // gsl
    const double y = gsl_sf_bessel_J0 (0.5);
    // jsoncpp
    Json::Value(1);
    // kafka
    const auto error = RdKafka::ErrorCode::ERR__BEGIN;
    // qt core
    const auto qtsring = QString::fromStdString("QString");
    // qt Gui
    const QBitmap bitmap();
    // qt Widgets
    const QCheckBox checkBox();
    // qt OpenGL
    const QOpenGLBuffer glBuffer();
    // qt Test
    const QTestEventList testEventList();
    // qt Help
    const QHelpSearchResult helpSearchResult();
    // qt Concurrent
    const auto unorderedReduce = QtConcurrent::UnorderedReduce;
    // qt Xml
    const QDomAttr attr();
    // qt WebKitWidgets
    const auto renderLayer = QWebFrame::RenderLayer::ContentsLayer;
    // qt Network
    const auto errorDns = QDnsLookup::Error::NoError;
    // qt PrintSupport
    const auto painterColourMode = QPrinter::ColorMode::Color;
    // qscintilla
    const QsciStyle sciStyle();
}

class MyTestSuite1 : public CxxTest::TestSuite
{
public:
    void testAddition(void)
    {
        TS_ASSERT(1 + 1 > 1);
        TS_ASSERT_EQUALS(1 + 1, 2);
    }
};
