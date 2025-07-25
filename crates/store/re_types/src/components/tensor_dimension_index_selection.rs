// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/rust/api.rs
// Based on "crates/store/re_types/definitions/rerun/components/tensor_dimension_selection.fbs".

#![allow(unused_braces)]
#![allow(unused_imports)]
#![allow(unused_parens)]
#![allow(clippy::clone_on_copy)]
#![allow(clippy::cloned_instead_of_copied)]
#![allow(clippy::map_flatten)]
#![allow(clippy::needless_question_mark)]
#![allow(clippy::new_without_default)]
#![allow(clippy::redundant_closure)]
#![allow(clippy::too_many_arguments)]
#![allow(clippy::too_many_lines)]

use ::re_types_core::try_serialize_field;
use ::re_types_core::SerializationResult;
use ::re_types_core::{ComponentBatch as _, SerializedComponentBatch};
use ::re_types_core::{ComponentDescriptor, ComponentType};
use ::re_types_core::{DeserializationError, DeserializationResult};

/// **Component**: Specifies a concrete index on a tensor dimension.
#[derive(Clone, Debug, Hash, Copy, PartialEq, Eq, Default)]
#[repr(transparent)]
pub struct TensorDimensionIndexSelection(pub crate::datatypes::TensorDimensionIndexSelection);

impl ::re_types_core::Component for TensorDimensionIndexSelection {
    #[inline]
    fn name() -> ComponentType {
        "rerun.components.TensorDimensionIndexSelection".into()
    }
}

::re_types_core::macros::impl_into_cow!(TensorDimensionIndexSelection);

impl ::re_types_core::Loggable for TensorDimensionIndexSelection {
    #[inline]
    fn arrow_datatype() -> arrow::datatypes::DataType {
        crate::datatypes::TensorDimensionIndexSelection::arrow_datatype()
    }

    fn to_arrow_opt<'a>(
        data: impl IntoIterator<Item = Option<impl Into<::std::borrow::Cow<'a, Self>>>>,
    ) -> SerializationResult<arrow::array::ArrayRef>
    where
        Self: Clone + 'a,
    {
        crate::datatypes::TensorDimensionIndexSelection::to_arrow_opt(data.into_iter().map(
            |datum| {
                datum.map(|datum| match datum.into() {
                    ::std::borrow::Cow::Borrowed(datum) => ::std::borrow::Cow::Borrowed(&datum.0),
                    ::std::borrow::Cow::Owned(datum) => ::std::borrow::Cow::Owned(datum.0),
                })
            },
        ))
    }

    fn from_arrow_opt(
        arrow_data: &dyn arrow::array::Array,
    ) -> DeserializationResult<Vec<Option<Self>>>
    where
        Self: Sized,
    {
        crate::datatypes::TensorDimensionIndexSelection::from_arrow_opt(arrow_data)
            .map(|v| v.into_iter().map(|v| v.map(Self)).collect())
    }
}

impl<T: Into<crate::datatypes::TensorDimensionIndexSelection>> From<T>
    for TensorDimensionIndexSelection
{
    fn from(v: T) -> Self {
        Self(v.into())
    }
}

impl std::borrow::Borrow<crate::datatypes::TensorDimensionIndexSelection>
    for TensorDimensionIndexSelection
{
    #[inline]
    fn borrow(&self) -> &crate::datatypes::TensorDimensionIndexSelection {
        &self.0
    }
}

impl std::ops::Deref for TensorDimensionIndexSelection {
    type Target = crate::datatypes::TensorDimensionIndexSelection;

    #[inline]
    fn deref(&self) -> &crate::datatypes::TensorDimensionIndexSelection {
        &self.0
    }
}

impl std::ops::DerefMut for TensorDimensionIndexSelection {
    #[inline]
    fn deref_mut(&mut self) -> &mut crate::datatypes::TensorDimensionIndexSelection {
        &mut self.0
    }
}

impl ::re_byte_size::SizeBytes for TensorDimensionIndexSelection {
    #[inline]
    fn heap_size_bytes(&self) -> u64 {
        self.0.heap_size_bytes()
    }

    #[inline]
    fn is_pod() -> bool {
        <crate::datatypes::TensorDimensionIndexSelection>::is_pod()
    }
}
