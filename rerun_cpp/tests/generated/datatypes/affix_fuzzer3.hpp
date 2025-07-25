// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/testing/datatypes/fuzzy.fbs".

#pragma once

#include "affix_fuzzer1.hpp"

#include <array>
#include <cstdint>
#include <cstring>
#include <memory>
#include <new>
#include <rerun/collection.hpp>
#include <rerun/result.hpp>
#include <utility>

namespace arrow {
    class Array;
    class DataType;
    class DenseUnionBuilder;
} // namespace arrow

namespace rerun::datatypes {
    namespace detail {
        /// \private
        enum class AffixFuzzer3Tag : uint8_t {
            /// Having a special empty state makes it possible to implement move-semantics. We need to be able to leave the object in a state which we can run the destructor on.
            None = 0,
            degrees,
            craziness,
            fixed_size_shenanigans,
            empty_variant,
        };

        /// \private
        union AffixFuzzer3Data {
            float degrees;

            rerun::Collection<rerun::datatypes::AffixFuzzer1> craziness;

            std::array<float, 3> fixed_size_shenanigans;

            AffixFuzzer3Data() {
                std::memset(reinterpret_cast<void*>(this), 0, sizeof(AffixFuzzer3Data));
            }

            ~AffixFuzzer3Data() {}

            void swap(AffixFuzzer3Data& other) noexcept {
                // This bitwise swap would fail for self-referential types, but we don't have any of those.
                char temp[sizeof(AffixFuzzer3Data)];
                void* otherbytes = reinterpret_cast<void*>(&other);
                void* thisbytes = reinterpret_cast<void*>(this);
                std::memcpy(temp, thisbytes, sizeof(AffixFuzzer3Data));
                std::memcpy(thisbytes, otherbytes, sizeof(AffixFuzzer3Data));
                std::memcpy(otherbytes, temp, sizeof(AffixFuzzer3Data));
            }
        };
    } // namespace detail

    struct AffixFuzzer3 {
        AffixFuzzer3() : _tag(detail::AffixFuzzer3Tag::None) {}

        /// Copy constructor
        AffixFuzzer3(const AffixFuzzer3& other) : _tag(other._tag) {
            switch (other._tag) {
                case detail::AffixFuzzer3Tag::craziness: {
                    using TypeAlias = rerun::Collection<rerun::datatypes::AffixFuzzer1>;
                    new (&_data.craziness) TypeAlias(other._data.craziness);
                } break;
                case detail::AffixFuzzer3Tag::degrees:
                case detail::AffixFuzzer3Tag::fixed_size_shenanigans:
                case detail::AffixFuzzer3Tag::empty_variant: {
                    const void* otherbytes = reinterpret_cast<const void*>(&other._data);
                    void* thisbytes = reinterpret_cast<void*>(&this->_data);
                    std::memcpy(thisbytes, otherbytes, sizeof(detail::AffixFuzzer3Data));
                } break;
                case detail::AffixFuzzer3Tag::None: {
                } break;
                default:
                    assert(false && "unreachable");
            }
        }

        AffixFuzzer3& operator=(const AffixFuzzer3& other) noexcept {
            AffixFuzzer3 tmp(other);
            this->swap(tmp);
            return *this;
        }

        AffixFuzzer3(AffixFuzzer3&& other) noexcept : AffixFuzzer3() {
            this->swap(other);
        }

        AffixFuzzer3& operator=(AffixFuzzer3&& other) noexcept {
            this->swap(other);
            return *this;
        }

        ~AffixFuzzer3() {
            switch (this->_tag) {
                case detail::AffixFuzzer3Tag::None: {
                    // Nothing to destroy
                } break;
                case detail::AffixFuzzer3Tag::degrees: {
                    // has a trivial destructor
                } break;
                case detail::AffixFuzzer3Tag::craziness: {
                    using TypeAlias = rerun::Collection<rerun::datatypes::AffixFuzzer1>;
                    _data.craziness.~TypeAlias();
                } break;
                case detail::AffixFuzzer3Tag::fixed_size_shenanigans: {
                    // has a trivial destructor
                } break;
                case detail::AffixFuzzer3Tag::empty_variant: {
                    // has a trivial destructor
                } break;
                default:
                    assert(false && "unreachable");
            }
        }

        void swap(AffixFuzzer3& other) noexcept {
            std::swap(this->_tag, other._tag);
            this->_data.swap(other._data);
        }

        AffixFuzzer3(float degrees) : AffixFuzzer3() {
            *this = AffixFuzzer3::degrees(std::move(degrees));
        }

        AffixFuzzer3(rerun::Collection<rerun::datatypes::AffixFuzzer1> craziness) : AffixFuzzer3() {
            *this = AffixFuzzer3::craziness(std::move(craziness));
        }

        AffixFuzzer3(std::array<float, 3> fixed_size_shenanigans) : AffixFuzzer3() {
            *this = AffixFuzzer3::fixed_size_shenanigans(std::move(fixed_size_shenanigans));
        }

        static AffixFuzzer3 degrees(float degrees) {
            AffixFuzzer3 self;
            self._tag = detail::AffixFuzzer3Tag::degrees;
            new (&self._data.degrees) float(std::move(degrees));
            return self;
        }

        static AffixFuzzer3 craziness(rerun::Collection<rerun::datatypes::AffixFuzzer1> craziness) {
            AffixFuzzer3 self;
            self._tag = detail::AffixFuzzer3Tag::craziness;
            new (&self._data.craziness)
                rerun::Collection<rerun::datatypes::AffixFuzzer1>(std::move(craziness));
            return self;
        }

        static AffixFuzzer3 fixed_size_shenanigans(std::array<float, 3> fixed_size_shenanigans) {
            AffixFuzzer3 self;
            self._tag = detail::AffixFuzzer3Tag::fixed_size_shenanigans;
            new (&self._data.fixed_size_shenanigans)
                std::array<float, 3>(std::move(fixed_size_shenanigans));
            return self;
        }

        static AffixFuzzer3 empty_variant() {
            AffixFuzzer3 self;
            self._tag = detail::AffixFuzzer3Tag::empty_variant;
            return self;
        }

        /// Return a pointer to degrees if the union is in that state, otherwise `nullptr`.
        const float* get_degrees() const {
            if (_tag == detail::AffixFuzzer3Tag::degrees) {
                return &_data.degrees;
            } else {
                return nullptr;
            }
        }

        /// Return a pointer to craziness if the union is in that state, otherwise `nullptr`.
        const rerun::Collection<rerun::datatypes::AffixFuzzer1>* get_craziness() const {
            if (_tag == detail::AffixFuzzer3Tag::craziness) {
                return &_data.craziness;
            } else {
                return nullptr;
            }
        }

        /// Return a pointer to fixed_size_shenanigans if the union is in that state, otherwise `nullptr`.
        const std::array<float, 3>* get_fixed_size_shenanigans() const {
            if (_tag == detail::AffixFuzzer3Tag::fixed_size_shenanigans) {
                return &_data.fixed_size_shenanigans;
            } else {
                return nullptr;
            }
        }

        /// Returns true if the union is in the empty_variant state.
        bool is_empty_variant() const {
            return _tag == detail::AffixFuzzer3Tag::empty_variant;
        }

        /// \private
        const detail::AffixFuzzer3Data& get_union_data() const {
            return _data;
        }

        /// \private
        detail::AffixFuzzer3Tag get_union_tag() const {
            return _tag;
        }

      private:
        detail::AffixFuzzer3Tag _tag;
        detail::AffixFuzzer3Data _data;
    };
} // namespace rerun::datatypes

namespace rerun {
    template <typename T>
    struct Loggable;

    /// \private
    template <>
    struct Loggable<datatypes::AffixFuzzer3> {
        static constexpr std::string_view ComponentType = "rerun.testing.datatypes.AffixFuzzer3";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype();

        /// Serializes an array of `rerun::datatypes::AffixFuzzer3` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const datatypes::AffixFuzzer3* instances, size_t num_instances
        );

        /// Fills an arrow array builder with an array of this type.
        static rerun::Error fill_arrow_array_builder(
            arrow::DenseUnionBuilder* builder, const datatypes::AffixFuzzer3* elements,
            size_t num_elements
        );
    };
} // namespace rerun
